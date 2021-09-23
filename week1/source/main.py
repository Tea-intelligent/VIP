import cv2
import utilities as util


if __name__ == "__main__":

    car_path = "vehicles/car.mp4"
    bus_path = "vehicles/bus.mp4"
    van_path = "vehicles/van.mp4"
    container_path = "vehicles/container.mp4"
    bulldozer_path = "vehicles/bulldozer.mp4"
    excavator_path = "vehicles/excavator.mp4"
    concrete_mixer_path = "vehicles/concrete_mixer.mp4"
    truck_path = "vehicles/truck.mp4"

    util.video_convert(car_path, 20, 5, "car/")
    util.video_convert(bus_path, 5, 10, "bus/")
    util.video_convert(van_path, 5, 10, "van/")
    util.video_convert(container_path, 5, 10, "container/")
    util.video_convert(bulldozer_path, 5, 10, "bulldozer/")
    util.video_convert(excavator_path, 5, 10, "excavator/")
    util.video_convert(concrete_mixer_path, 5, 10, "concrete_mixer/")
    util.video_convert(truck_path, 5, 10, "truck/")

    img = cv2.imread("Lenna.png")

    g_img = util.gray_convert(img)

    cv2.imshow("Grayscale picture", g_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
