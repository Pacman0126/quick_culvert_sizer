"""
The target audience for this app is anyone with a civil engineering
background. In the civil engineering consulting sector, chasing new
projects with proposals is routine. In this phase, the team needs to
put together a preliminary design for the tender process of a RFP
(Request for Proposal)and submit a preliminary cost estimate as a
part of this. At this stage, project engineers will need to create a
drainage area map of all the catchments touching the project site (for
roadway projects this could be up to 20 miles, sometimes more with dozens
of stream crossings) from contour maps which can take a few days. As part
of this, a diligent civil engineer will analyse and comupute the time-of-
concentration (Tc) for each drainage area. This is a dreaded task because
it is part art part science and takes some intuition from experience from
interpreting contour maps, so it is often put off to the last minute. The
time-of-concentration is the time in minutes for a raindrop to travel, from
the most remote point and most likely path, to the point of interest and
breaking the path up into sections to compute the travel time.

With quick-culvert-sizer and once the time-of-concentration's are known
(generally a few days) the user can use the results of this app to quickly
select a reasonable design after inputting the relevant information (size
of catchment area, properties of the catchment from soil maps, contourmaps,
satellite immages, etc, size constraints of box-culvert, targeted flow
velocity inside this structure). No more "seat-of-the-pants" risky guessing.
This app can perform up to 490 iterations to zero in on an economically
efficient size. This each iteration is equivalent to 490 spreadsheet
iterations for a single box-culvert and is also error prone.
"""

import math
import ast
import sys


def get_box_culvert_options():
    """
    This function obtains design constraints from the user and
    uses this input to run the algorithhm iterations.
    """

    max_box_height = 0

    query = ""

    query2 = ""

    # fetch all properties of catchment
    catchment_area_properties = get_catchment_area_properties()

    catchment_area = catchment_area_properties[0]

    tc_vs_area = catchment_area_properties[1]

    runoff_coefficient = catchment_area_properties[2]

    assumed_flow_velocity = 5.0

    message = (
        f"The default assumed flow velocity for box culverts is \
        {assumed_flow_velocity} ft/s.\nA minimum of 2.5 ft/s is  \
        required to be self cleaning, a maximum of 8.0 ft/s is \
        allowed to prevent downstream erosion damage.\n Enter new \
        value or press <enter> to continue with default value: "
    )

    while True:

        try:

            query2 = input(message)

            if not query2:

                assumed_flow_velocity = 5.0

                break

            for (
                char
            ) in query2:  # replace ',' with '.' as decimal symbol if needed

                if char == ",":

                    query2 = query2.replace(",", ".")

                    print(
                        "\nComma detetected as decimal place and replaced "
                        "with '.'"
                    )

            number_of_decimal_places = []

            for char in query2:  # count number of decimal symbols in input

                if char == ".":

                    number_of_decimal_places.append(char)

            if len(number_of_decimal_places) > 1:

                print(
                    "\nThousand's separator detected and not allowed."
                    "Value can be 2.5 to 8.0. For example, 2.500 is "
                    "\ninterpreted as 2.5 ft/s not 2500 ft/s. or 2,500.0"
                    "will be interpreted as 2500.0 ft/s and above 8.0 ft/s\n")

                raise ValueError

            query2 = ast.literal_eval(query2)

            if (not isinstance(query2, float)) and (
                not isinstance(query2, int)
            ):

                raise ValueError

            assumed_flow_velocity = query2

            if float(query2) < 2.5 or float(query2) > 8.0:

                print("")

                print("Enter value between 2.5 and 8.0")

                print("")

                query2 = input(message)

                continue

            assumed_flow_velocity = float(query2)

            break

        except ValueError:

            print("Invalid input. Must be number between 2.5 and 8.0\n")

            continue

        except KeyboardInterrupt:

            print("Interrupted, exiting application")

            return

    while True:

        scenario = ""

        try:
            str_max_box_height = input(
                "\nAt this culvert location, what is the "
                "maximum height up to 10 the box culvert can be: "
            )

            if not str_max_box_height:

                raise ValueError  # user hit enter without a value

            for (
                char
            ) in str_max_box_height:  # check is integer whole number was input

                if char == ",":

                    raise ValueError

            str_max_box_height = ast.literal_eval(str_max_box_height)

            if not isinstance(str_max_box_height, int):

                raise ValueError

            if int(str_max_box_height) < 4 or int(str_max_box_height) > 10:

                if int(str_max_box_height) < 4:

                    scenario = "1"

                elif int(str_max_box_height) > 10:

                    scenario = "2"

                match scenario:

                    case "1":

                        while True:

                            try:

                                query = input(
                                    "Box culverts should have a minimum "
                                    "height of 4 ft. Would you like to use a "
                                    "different height (y/n): "
                                )

                                if query in set(["y", "Y"]):

                                    break

                                if query in set(["n", "N"]):

                                    print(
                                        "Try circular pipe instead. This "
                                        "application is for box culverts "
                                        "only.")

                                    return

                                raise ValueError

                            except ValueError:

                                print("\nInvalid input. Must be y or n\n")

                                continue

                        continue

                    case "2":

                        while True:

                            try:

                                query = input(
                                    "\nPrecast box culverts should not be "
                                    "more than 10 ft tall due to roadway lane"
                                    " widths while being delivered.\nWould you"
                                    " like to use a different height (y/n):")

                                if query in set(["y", "Y"]):

                                    break

                                if query in set(["n", "N"]):

                                    print(
                                        "Try circular pipe instead. This "
                                        "application is "
                                        "for box culverts only.")

                                    return

                                raise ValueError

                            except ValueError:

                                print("\nInvalid input. Must be y or n\n")

                                continue

                        continue
            else:

                max_box_height = int(str_max_box_height)

                print(" ")

                break

        except ValueError:

            print(
                "\nInvalid input. Must be increments of ft. from 4, 5, 6,...10"
            )

            continue

        except KeyboardInterrupt:

            print("Interrupted, exiting application")

            return

    # Manning's formula for open channel flow in culvert structures and
    # water channels: Q = A * 1.486/n * R^(2/3) * S^(1/2)
    #
    # Q = Discharge (cu. ft./sec.) --> box_dimen_vs_flow_capacity{}
    # A = Cross-sectional Area of Flow (sq. ft.) --> box_flow_area
    # n = Coefficient of Roughness --> n = 0.012 for concrete
    # R = Hydraulic Radius (ft.) = P/A --> hydraulic_radius
    # S = Slope of Pipe (ft./ft.) --> slopes[]
    # P = Wetted perimeter (ft.) --> wetted_perimeter

    n = 0.012  # value for concrete

    slopes = []

    slopes = [round(0.0120 + (s * 0.0005), 4) for s in range(1, 37)]

    barrel_count = 0

    # vvvv begin main algorithim vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

    # The code block below now drills down on all the solution possibilites
    # found above and finds the smallest(i.e. most ecenoical) box culvert
    # solution in each time of concentration, Tc, and collects them into a
    # dictionary with key=Tc, value=(width,height)

    print(f"Catchment area size = {catchment_area} acres")

    print(
        f"Composite runoff coefficient for this catchment area = \
        {runoff_coefficient}"
    )

    print(
        f"assumed flow velocity in box culvert = {assumed_flow_velocity} ft/s"
    )

    print("")

    box_dimen_vs_flow_capacity = {}

    # this is the total area of all barrels
    box_dimen_total_cross_sectional_area = {}

    # this is the number of barrels for each box dimension
    box_dimen_number_of_barrels = {}

    s_barrels = {}

    for time_of_concentration_in_minutes in range(10, 110, 10):

        for box_height in range(4, max_box_height + 1, 1):

            for span in range(box_height, 11, 1):

                # The code block below iterates thru s_barrels{} and extracts
                # the number of  barrrels required for each slope condition
                # 1.25% to 3.00% and finds the  number of barrels that appears
                # in this range. Then adds the maximum number of occurences
                # (e.g. out of 4,5,6 barrels 5 appears 20 times out of 36 slope
                # conditions). The box size 5 ft x 4 ft as key with value=3 is
                # added to dictionary of solutions{} as (5,4):3

                box_flow_area = span * (box_height - 1.5)

                wetted_perimeter = (box_height - 1.5) * 2 + span

                hydraulic_radius = box_flow_area / wetted_perimeter

                for slope in slopes:

                    flow_capactiy = round(
                        (1.486 / n)
                        * box_flow_area
                        * math.pow(hydraulic_radius, (2 / 3))
                        * math.pow(slope, 0.5),
                        1,
                    )

                    required_cross_sectional_area = (
                        flow_capactiy / assumed_flow_velocity
                    )

                    s_barrels.update(
                        {
                            slope: math.ceil(
                                tc_vs_area[time_of_concentration_in_minutes]
                                / required_cross_sectional_area
                            )
                        }
                    )

                box_dimen_vs_flow_capacity.update(
                    {(span, box_height): s_barrels}
                )

                number_of_barrels = (
                    []
                )  # list of all barrel counts in slope range

                barrel_count_vs_frequency = {}

                for key in s_barrels.items():

                    number_of_barrels.append(key[1])

                # iterate thru width number of required barrels 1 to 10.
                for x in range(1, 11):
                    # typically not more than 6 barrels
                    if number_of_barrels[x] == 0:

                        continue

                    if number_of_barrels.count(x) == 0:

                        continue

                    barrel_count_vs_frequency.update(
                        {x: number_of_barrels.count(x)}
                    )

                most_frequent_barrel_num = max(
                    barrel_count_vs_frequency,
                    key=barrel_count_vs_frequency.get,
                )

                box_dimen_total_cross_sectional_area.update(
                    {
                        (span, box_height): most_frequent_barrel_num
                        * span
                        * box_height
                    }
                )

                box_dimen_number_of_barrels.update(
                    {(span, box_height): most_frequent_barrel_num}
                )
                s_barrels = {}

        barrel_count = box_dimen_number_of_barrels.get((span, box_height))

        most_econonomical_design = min(
            box_dimen_total_cross_sectional_area,
            key=box_dimen_total_cross_sectional_area.get,
        )

        design_span = most_econonomical_design[0]

        design_height = most_econonomical_design[1]

        message_pt1 = f"Most econonomical design for Tc = \
        {time_of_concentration_in_minutes} is"

        message_pt2 = f" {barrel_count} - {design_span}  ft (span) x \
        {design_height} ft (height) "

        print(message_pt1 + message_pt2)

        box_dimen_total_cross_sectional_area = {}

        box_dimen_number_of_barrels = {}

    # ^^^^^^^^^^^^^ end main algorithm ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    print("")

    while True:

        try:

            query1 = input(
                "Do you have any more catchments to consider (y/n): "
            )

            if not query1:
                raise ValueError

            if query1 in set(["y", "Y"]):

                get_box_culvert_options()

            elif query1 in set(["n", "N"]):

                return

            else:
                raise ValueError

        except ValueError:

            print("\nInvalid input.")

            continue

        except KeyboardInterrupt:

            print("Interrupted, exiting application")

            return


def get_catchment_area_properties(flow_velocity=None):
    """
    The catchment charactersistics for the catchment of interest are
    calculated based on user input of catchment area
    """

    while True:

        try:

            str_catchment_area = input(
                "Input size of catchment in acres. "
                "Maximum area is 200 acres: "
            )

            if not str_catchment_area:

                raise ValueError

            for (
                char
            ) in (
                str_catchment_area
            ):  # replace ',' with '.' as decimal symbol if needed

                if char == ",":

                    str_catchment_area = str_catchment_area.replace(",", ".")

                    print(
                        "\nComma detetected as decimal place and replaced "
                        "with '.'"
                    )

                    break

            number_of_decimal_places = []

            for (
                char
            ) in (
                str_catchment_area
            ):  # count number of decimal symbols in input

                if char == ".":

                    number_of_decimal_places.append(char)

            if len(number_of_decimal_places) > 1:

                print(
                    "\nThousand's separator detected and not allowed."
                    "Value can be up to 200.0. For example, \n2.000 is "
                    "interpreted as 2 acres not 2000 acres or 2,500.0 is "
                    "interpreted as 2500.0 acres \nand beyond the 200.0 "
                    "acre limit.")

                raise ValueError

            str_catchment_area = ast.literal_eval(str_catchment_area)

            if (not isinstance(str_catchment_area, float)) and (
                not isinstance(str_catchment_area, int)
            ):

                raise ValueError

            catchment_area = float(str_catchment_area)

            if (
                catchment_area <= 0 or catchment_area > 200
            ):  # analysis only valid up to 200 ac
                print(
                    "\nInvalid input, size must be acres a whole number\n "
                    "or decimal greater than zero and not more than 200 acres"
                )

                continue

        except ValueError:

            print(
                "\nInvalid input, size must be acres a whole number "
                "or decimal."
            )

            continue

        except KeyboardInterrupt:

            print("Interrupted, exiting application")

            sys.exit(0)

        else:

            break

    catchment_area = float(round(catchment_area, 1))

    # these constants come from https://hdsc.nws.noaa.gov/pfds/
    # for Dallas County 5-year storm

    e = 0.8052
    b = 68.99
    d = 9.76

    if flow_velocity is None:

        assumed_flow_velocity = 5.0

    else:
        assumed_flow_velocity = flow_velocity

    print(" ")

    # call sub-function to compute runoff coefficient
    runoff_coefficient = get_runoff_coefficient()

    tc_vs_area = {}

    tc_vs_area = {
        time_of_concentration_in_minutes: round(
            (
                runoff_coefficient
                * b
                / math.pow((time_of_concentration_in_minutes + d), e)
                * catchment_area
                / assumed_flow_velocity
            ),
            1,
        )
        for time_of_concentration_in_minutes in range(10, 110, 10)
    }

    # bundle catchment properties and return back to calling function
    return (catchment_area, tc_vs_area, runoff_coefficient)


def get_runoff_coefficient():
    """
    This function builds a runoff coefficient for rural watersheds based on
    a methodology from Texas Department of Transportation's Hydraulic Design
    Manual and stores in a global variable since it is a critical value that
    needs to be available throughout the application.
    """

    # Watershed relief characteristics.

    relief_component = 0.0

    print("[1] - Extreme: Steep, rugged terrain with average slopes above 30%")

    print("[2] - High: Hilly, with average slopes of 10-30%")

    print("[3] - Normal: Rolling, with average slopes of 5-10%")

    print("[4] - Low: Relatively flat land, with average slopes of 0-5%\n")

    while True:

        try:
            str_cr = input(
                "What are the watershed relief characteristics of"
                " this catchment area. Select from above: "
            )

            if not str_cr:

                raise ValueError  # user hit enter without a value

            if (
                len(str_cr) != 1
            ):  # test for leading whitespace, decimal point or negative number

                raise ValueError

            if not str_cr.isdigit():  # is user input numerical

                raise ValueError

            if int(str_cr) < 1 or int(str_cr) > 4:

                print("\nNot a valid selection. Selection not available.\n")

                continue

        except ValueError:

            print("\nInvalid input. Must be a single digit from 1, 2, 3, 4\n")

            continue

        except KeyboardInterrupt:

            print("Interrupted, exiting application")

            sys.exit(0)

        else:
            print(" ")

            break

    match str_cr:

        case "1":

            relief_component = 0.315

        case "2":

            relief_component = 0.24

        case "3":

            relief_component = 0.17

        case "4":

            relief_component = 0.11

    # Watershed soil infiltration characteristics.

    infiltration_component = 0.0

    print(
        "[1] - Extreme: No effective soil cover; either rock or thin soil "
        "mantle of negligible infiltration capacity")

    print(
        "[2] - High: Slow to take up water, clay or shallow loam soils of low"
        " infiltration capacity or poorly drained"
    )

    print(
        "[3] - Normal: Normal; well drained light or medium textured soils, "
        "sandy loams"
    )

    print(
        "[4] - Low: Deep sand or other soil that takes up water readily; "
        "very light, well-drained soils\n"
    )

    while True:

        try:
            str_ci = input(
                "What are the watershed soil infiltration characteristics "
                "of this catchment area. Select from above: ")

            if not str_ci:

                raise ValueError  # user hit enter without a value

            if (
                len(str_ci) != 1
            ):  # leading whitespace in entry or negative number

                raise ValueError

            if not str_ci.isdigit():  # is user input numerical

                raise ValueError

            if int(str_ci) < 1 or int(str_ci) > 4:

                print("\nNot a valid selection. Selection not available.\n")

                continue

        except ValueError:

            print("\nInvalid input. Must be a single digit from 1, 2, 3, 4\n")

            continue

        except KeyboardInterrupt:

            print("Interrupted, exiting application")

            sys.exit(0)

        else:
            print(" ")

            break

    match str_ci:

        case "1":

            infiltration_component = 0.14

        case "2":

            infiltration_component = 0.10

        case "3":

            infiltration_component = 0.07

        case "4":

            infiltration_component = 0.05

    # Watershed Vegetal cover characteristics.

    vegetal_component = 0.0

    print("[1] - Extreme: No effective plant cover, bare or very sparse cover")

    print(
        "[2] - High: Poor to fair; clean cultivation, crops or poor natural "
        "cover, less than 20% of drainage area has good cover")

    print(
        "[3] - Normal: Fair to good; about 50% of area in good grassland or "
        "woodland, not more than 50% of area in cultivated crops")

    print(
        "[4] - Low: Good to excellent; about 90% of drainage area in good "
        "grassland, woodland, or equivalent cover\n")

    while True:

        try:
            str_cv = input(
                "What are the watershed vegetation characteristics of this "
                "catchment area. Select from above: "
            )

            if not str_cv:

                raise ValueError  # user hit enter without a value

            if (
                len(str_cv) != 1
            ):  # leading whitespace in entry or negative number

                raise ValueError

            if not str_cv.isdigit():  # is user input numerical

                raise ValueError

            if int(str_cv) < 1 or int(str_cv) > 4:

                print("\nNot a valid selection. Selection not available.\n")

                continue

        except ValueError:

            print("\nInvalid input. Must be a single digit from 1, 2, 3, 4\n")

            continue

        except KeyboardInterrupt:

            print("Interrupted, exiting application")

            sys.exit(0)

        else:
            print(" ")

            break

    match str_cv:

        case "1":

            vegetal_component = 0.14

        case "2":

            vegetal_component = 0.10

        case "3":

            vegetal_component = 0.07

        case "4":

            vegetal_component = 0.05

    # Watershed surface storage characteristics.

    surface_storage_component = 0.0

    print(
        "[1] - Extreme: Negligible; surface depressions few and shallow, "
        "drainageways steep and small, no marshes")

    print(
        "[2] - High: Well-defined system of small drainageways, no ponds "
        "or marshes"
    )

    print(
        "[3] - Normal: Normal; considerable surface depression, e.g., storage "
        "lakes and ponds and marshes"
    )

    print(
        "[4] - Low: Much surface storage, drainage system not sharply "
        "defined; large floodplain storage, large number of ponds or  "
        "marshes\n")

    while True:

        try:
            str_cs = input(
                "What are the watershed surface storage characteristics of "
                "this catchment area. Select from above: "
            )

            if not str_cs:

                raise ValueError  # user hit enter without a value

            if (
                len(str_cs) != 1
            ):  # leading whitespace in entry or negative number

                raise ValueError

            if not str_cs.isdigit():  # is user input numerical

                raise ValueError

            if int(str_cs) < 1 or int(str_cs) > 4:

                print("\nNot a valid selection. Selection not available.\n")

                continue

        except ValueError:

            print("\nInvalid input. Must be a single digit from 1, 2, 3, 4\n")

            continue

        except KeyboardInterrupt:

            print("Interrupted, exiting application")

            sys.exit(0)

        else:
            print(" ")

            break

    match str_cs:

        case "1":

            surface_storage_component = 0.11

        case "2":

            surface_storage_component = 0.09

        case "3":

            surface_storage_component = 0.07

        case "4":

            surface_storage_component = 0.05

    runoff_coefficient = round(
        relief_component
        + infiltration_component
        + vegetal_component
        + surface_storage_component,
        2,
    )

    return runoff_coefficient


def main():
    """
    This is the main() function where the initial function call is made
    """
    get_box_culvert_options()


main()
