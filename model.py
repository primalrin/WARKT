import numpy as np
import matplotlib.pyplot as plt

def rocket_simulation(duration, dt, initial_fuel_mass):
    # Параметры ракеты и окружающей среды
    initial_rocket_mass = 552255.0  # начальная масса ракеты в кг
    gravity = 9.81  # ускорение свободного падения в м/с^2
    drag_coefficient = 0.1  # коэффициент сопротивления воздуха
    cross_sectional_area = 47.78  # в квадратных метрах
    thrust = 7805460.0  # сила тяги ракеты в Н
    fuel_consumption_rate = 6254.875  # скорость истечения топлива в кг/с
    # Начальные условия
    initial_height = 0.0  # начальная высота в м
    initial_speed = 0.0  # начальная скорость в м/с
    initial_fuel = initial_fuel_mass  # начальная масса топлива в кг

    # Инициализация массивов для записи данных
    time_values = np.arange(0, duration, dt)
    height_values = np.zeros_like(time_values)
    speed_values = np.zeros_like(time_values)
    fuel_mass_values = np.zeros_like(time_values)

    # Начальные условия
    height = initial_height
    speed = initial_speed
    fuel_mass = initial_fuel

    # Моделирование движения ракеты
    for i in range(len(time_values)):
        # Запись данных
        height_values[i] = height
        speed_values[i] = speed
        fuel_mass_values[i] = fuel_mass
        # Сила тяжести
        gravity_force = initial_rocket_mass * gravity * (600000 / (600000 + height))
        # Сила сопротивления воздуха
        current_density = interpolate_density(height)  # Интерполяция плотности по высоте
        air_resistance = 0.5 * current_density * speed**2 * drag_coefficient * cross_sectional_area 
        # # Проверка наличия топлива
        # if fuel_mass > 0:
        #     thrust -= fuel_consumption_rate  # уменьшаем тягу на скорость истечения топлива
        #     fuel_mass -= fuel_consumption_rate * dt  # уменьшаем массу топлива

        # else:
        #     thrust = 0.0  # если топливо закончилось, тяга равна нулю

        # Уравнение движения
        acceleration = (thrust - gravity_force - air_resistance) / (initial_rocket_mass)
        speed += acceleration * dt
        height += speed * dt

        

        # Проверка, если ракета достигла земли (высота стала отрицательной), прерываем моделирование
        if height < 0:
            break
    return time_values[:i+1], height_values[:i+1], speed_values[:i+1], fuel_mass_values[:i+1]

# Интерполяция плотности по высоте
def interpolate_density(height):
    # Данные из предоставленной таблицы
    heights = [0, 2500, 5000, 7500, 10000, 15000, 20000, 25000, 30000, 40000, 50000, 60000, 70000]
    densities = [1.225, 0.898, 0.642, 0.446, 0.288, 0.108, 0.040, 0.015, 0.006, 0.001, 0.000, 0.000, 0.000]

    return np.interp(height, heights, densities)

# Время моделирования и шаг по времени
total_duration = 130  # секунд
time_step = 5  # секунды
initial_fuel_mass = 25500   # начальная масса топлива в кг

# Запуск симуляции
time, height, speed, fuel_mass = rocket_simulation(total_duration, time_step, initial_fuel_mass)
# Построение графиков
plt.figure(figsize=(22, 11))

plt.subplot(2, 1, 1)
plt.plot(time, height)
plt.title('Высота от времени')
plt.xlabel('Время (с)')
plt.ylabel('Высота (м)')

plt.subplot(2, 1, 2)
plt.plot(time, speed)
plt.title('Скорость от времени')
plt.xlabel('Время (с)')
plt.ylabel('Скорость (м/с)')


plt.tight_layout()
plt.show()
