
def find_index_of_darkest_street_light(road_length: int, not_working_street_lights: list[int]) -> int:
    lights_to_change = []
    all_illuminations = all_illuminations_list(road_length)
    darkest_index = -1
    lowest_intensity_illumination = 2000000
    for i in not_working_street_lights:
        forward_illumination_distance = forward_lights(i, all_illuminations, not_working_street_lights)
        backward_illumination_distance = backward_lights(i, all_illuminations, not_working_street_lights)
        illumination_distance = get_distance(forward_illumination_distance, backward_illumination_distance)
        intensity_illumination = calculate_intensity_illumination(illumination_distance)
        if intensity_illumination < 0.01:
            continue
        if intensity_illumination < 1:
            lights_to_change.append(i)
        if lowest_intensity_illumination == intensity_illumination:
            darkest_index = min(darkest_index, i)
        if lowest_intensity_illumination > intensity_illumination:
            lowest_intensity_illumination = intensity_illumination
            darkest_index = i
    print("lighting " + ", ".join(map(str, lights_to_change)) +
          " need to be replaced. In total " + str(len(lights_to_change)) + " light(s) need to change.")
    return darkest_index


def calculate_intensity_illumination(distance):
    return 3 ** (-(distance / 90) ** 2)


def all_illuminations_list(road_length: int):
    return list(range((road_length // 20) + 1))


def forward_lights(x, all_illuminations, not_working_street_lights: list[int]):
    distance = 0
    lights_to_check = list(range(x + 1, len(all_illuminations)))
    all_in_list = all(item in not_working_street_lights for item in lights_to_check)
    if all_in_list:
        return 0
    for i in range(x + 1, len(all_illuminations)):
        distance += 20
        if i not in not_working_street_lights:
            break
    return distance


def backward_lights(x, all_illuminations, not_working_street_lights: list[int]):
    distance = 0
    lights_to_check = list(range(x - 1, all_illuminations[0], -1))
    all_in_list = all(item in not_working_street_lights for item in lights_to_check)
    if all_in_list:
        return 0
    for i in range(x - 1, all_illuminations[0], -1):
        distance += 20
        if i not in not_working_street_lights:
            break
    return distance


def get_distance(forward_distance, backward_distance):
    if forward_distance == 0 or backward_distance == 0:
        return max(forward_distance, backward_distance)
    else:
        return min(forward_distance, backward_distance)


if __name__ == "__main__":
    # This is an example test. When evaluating the task, more will be added:
    assert find_index_of_darkest_street_light(road_length=200, not_working_street_lights=[4, 5, 6]) == 5
    assert find_index_of_darkest_street_light(road_length=200, not_working_street_lights=[4, 5]) == 4
    assert find_index_of_darkest_street_light(road_length=200, not_working_street_lights=[4]) == 4
    assert find_index_of_darkest_street_light(road_length=200, not_working_street_lights=[4, 5, 6, 9]) == 5
    assert find_index_of_darkest_street_light(road_length=200, not_working_street_lights=[4, 6, 9]) == 4
    assert find_index_of_darkest_street_light(road_length=200, not_working_street_lights=[4, 5, 9]) == 4
    assert find_index_of_darkest_street_light(road_length=200, not_working_street_lights=[1, 4, 5, 6, 7, 9, 10]) == 5
    assert find_index_of_darkest_street_light(road_length=200, not_working_street_lights=[1, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert find_index_of_darkest_street_light(road_length=200, not_working_street_lights=[1, 2, 3, 4, 5, 6, 7, 10]) == 1
    assert find_index_of_darkest_street_light(road_length=200, not_working_street_lights=[1, 4, 5, 6, 7, 8, 9]) == 6
    assert find_index_of_darkest_street_light(road_length=200, not_working_street_lights=[2, 3, 4, 5, 6, 7, 10]) == 4
    print("ALL TESTS PASSED")
