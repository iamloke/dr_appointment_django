import random
import numpy as np
from datetime import timedelta
from doctors.models import DoctorProfile
from schedules.models import Schedule, Shift

class AppointmentOptimization:
    MAX_ITER = 100  # Maximum number of iterations
    POP_SIZE = 10  # Population size of whales
    DIM = 3  # Dimensions (e.g., Doctor, Shift, Time Slot)
    TIME_LIMIT = 17  # Latest appointment time is 17:00
    TIME_STEP = timedelta(minutes=30)  # Each appointment step (can be adjusted)

    # Initializing the WOA population
    # A whale is represented by a vector: [doctor_id, shift_id, time_slot]
    def initialize_population():
        population = []
        for _ in range(POP_SIZE):
            doctor = random.choice(DoctorProfile.objects.all())
            shift = random.choice(Shift.objects.all())
            time_slot = random.randint(9, TIME_LIMIT - 1)  # 9 to 17 hour range
            population.append([doctor.id, shift.id, time_slot])
        return population

    # Fitness function to evaluate an appointment scheduling solution
    def fitness(solution):
        doctor_id, shift_id, time_slot = solution
        doctor = DoctorProfile.objects.get(id=doctor_id)
        shift = Shift.objects.get(id=shift_id)
        
        # Check if the doctor is available at the selected time
        schedule = Schedule.objects.filter(doctor=doctor, shift=shift).first()
        
        if not schedule:
            return float('inf')  # Doctor not available at the given time
        
        # Check if the time slot is already taken
        if Appointment.objects.filter(schedule=schedule, time_slot=time_slot).exists():
            return float('inf')  # Appointment slot is taken
        
        # Calculate the fitness
        return fitness

    # Update position of a whale (solution) using WOA principles
    def update_position(whale, best_position, a, A, C, p, b):
        # Calculate the new position based on the WOA formula
        if random.random() < p:
            # Spiral update
            distance = np.abs(b * best_position - whale)
            new_position = whale + A * distance  # Whale moves in the spiral pattern
        else:
            # Exploitative search: search around the best solution
            r = np.random.random()  # Random value for exploration/exploitation
            new_position = best_position - A * np.abs(C * best_position - whale)  # Converge toward best solution

        # Ensure new position is within bounds (e.g., doctors, shifts, and time slots)
        new_position[0] = max(0, min(new_position[0], len(Doctor.objects.all()) - 1))
        new_position[1] = max(0, min(new_position[1], len(Shift.objects.all()) - 1))
        new_position[2] = max(9, min(new_position[2], 17))  # Time slots between 9 and 17

        return new_position

    # Main loop for WOA algorithm
    def whale_optimization():
        # Initialize population
        population = initialize_population()

        # Best solution initialization
        best_position = None
        best_fitness = float('inf')

        for t in range(MAX_ITER):
            # Calculate fitness for each whale (solution)
            fitness_values = [fitness(whale) for whale in population]
            
            # Update the best solution
            min_fitness = min(fitness_values)
            best_whale = population[fitness_values.index(min_fitness)]
            
            if min_fitness < best_fitness:
                best_fitness = min_fitness
                best_position = best_whale

            # Update whale positions based on the best solution found
            a = 2 - t * (2 / MAX_ITER)  # Decreasing factor
            A = 2 * a * random.random() - a  # Coefficient A
            C = 2 * random.random()  # Coefficient C
            p = random.random()  # Probability for exploration vs. exploitation
            b = 1  # A constant related to the spiral movement

            # Update each whale's position
            for i in range(POP_SIZE):
                population[i] = update_position(population[i], best_position, a, A, C, p, b)

        # Return the best solution found
        return best_position  # Best doctor, shift, and time slot

    # Final function to schedule an appointment
    def schedule_best_appointment():
        # Run WOA to find the best appointment schedule
        best_solution = whale_optimization()
        doctor_id, shift_id, time_slot = best_solution
        
        doctor = Doctor.objects.get(id=doctor_id)
        shift = Shift.objects.get(id=shift_id)
        
        # Check for available slot and create the appointment
        schedule = Schedule.objects.filter(doctor=doctor, shift=shift).first()
        
        if schedule and not Appointment.objects.filter(schedule=schedule, time_slot=time_slot).exists():
            # Assign a patient to this slot (patient details can be passed here)
            patient = Patient.objects.first()  # This can be modified as per your use case
            appointment = Appointment.objects.create(patient=patient, schedule=schedule, time_slot=time_slot)
            return appointment
        else:
            # No available slot
            return None

