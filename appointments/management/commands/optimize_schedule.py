from django.core.management.base import BaseCommand
from patients.models import PatientProfile
from doctors.models import DoctorProfile
from schedules.models import Schedule
from appointments.whale_optimization import WhaleOptimization

class Command(BaseCommand):
    help = 'Optimize doctor appointments using WOA'

    def handle(self, *args, **kwargs):
        # Load your data: patients, doctors, shifts, etc.
        patients = PatientProfile.objects.all()
        doctors = DoctorProfile.objects.all()
        schedules = Schedule.objects.all()

        # Define constraints and other parameters
        constraints = [(0, 10), (0, 5)]  # Example constraints
        nsols = 50  # Number of solutions
        b = 1.0  # b parameter for WOA
        a = 2.0  # a parameter for WOA
        a_step = 0.1  # Step size for a

        # Initialize the WhaleOptimization algorithm with the patients and schedules
        woa = WhaleOptimization(
            opt_func=self.fitness_function,
            constraints=constraints,
            nsols=nsols,
            b=b,
            a=a,
            a_step=a_step,
            maximize=False,
            patients=patients,  # Pass patients here
            schedules=schedules,  # Pass schedules here
            schedule_start_time=9.0,
            schedule_end_time=17.0
        )

        # Run the optimization
        woa.optimize()

        # Print best solution
        woa.print_best_solutions()

        # Once optimized, store the results back into your models
        best_schedule = woa._best_solutions[0]
        for patient, schedule, appointment_time in best_schedule:
            # Create appointment based on the optimized schedule
            Appointment.objects.create(patient=patient, schedule=schedule, appointment_time=appointment_time)

    def fitness_function(solutions, doctor_schedules):
        total_waiting_time = 0
        total_unutilized_time = 0

        for solution in solutions:
            patient, schedule, appointment_time = solution
            # Calculate waiting time (difference from preferred time)
            waiting_time = (appointment_time - patient.preferred_time).total_seconds()
            total_waiting_time += abs(waiting_time)

            # Maximize doctor utilization
            if schedule.doctor in doctor_schedules:
                total_unutilized_time += max(0, (schedule.shift.end_time - schedule.shift.start_time).seconds - len(doctor_schedules[schedule.doctor]))

        return total_waiting_time + total_unutilized_time
