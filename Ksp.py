import krpc
import time
import matplotlib.pyplot as plt

def main():
    # Подключение к серверу kRPC
    connection = krpc.connect(name='KSP Monitor')

    # Получение объекта весплавающей точки (Vessel)
    vessel = connection.space_center.active_vessel

    # Инициализация списков для хранения данных
    time_data = []
    velocity_data = []
    altitude_data = []

    try:
        # Основной цикл программы
        while time.sleep(130):
            # Получение и запись текущей скорости
            velocity = vessel.flight().speed
            velocity_data.append(velocity)

            # Получение и запись текущего времени
            current_time = connection.space_center.ut
            time_data.append(current_time)

            # Получение и запись текущей высоты
            altitude = vessel.flight().mean_altitude
            altitude_data.append(altitude)

            # Задержка перед следующим измерением
            time.sleep(1)

    except KeyboardInterrupt:
        print('Программа завершена пользователем.')

    finally:
        # Закрытие соединения с сервером kRPC
        connection.close()

        # Построение графиков
        plot_graph(time_data, velocity_data, 'Time (seconds)', 'Velocity (m/s)', 'Velocity vs Time')
        plot_graph(time_data, altitude_data, 'Time (seconds)', 'Altitude (meters)', 'Altitude vs Time')

def plot_graph(x_data, y_data, x_label, y_label, title):
    plt.plot(x_data, y_data)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()

if __name__ == '__main__':
   main()
