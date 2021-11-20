

def fractional(data_list, W):

    remaining_weight = int(W)
    total_weight = 0
    total_profit = 0

    data_list.sort(key=lambda x: x[2], reverse=True)

    for data in data_list:
        if remaining_weight <= 0:
            break
        if data[0] + total_weight <= W:
            total_weight += data[0]
            remaining_weight -= data[0]
            total_profit += data[1]
        else:
            profit_fraction = (remaining_weight/data[0])*data[1]
            weight_fraction = (remaining_weight/data[0])*data[0]
            remaining_weight -= remaining_weight
            total_weight += weight_fraction
            total_profit += profit_fraction
            break

    print('===================================================================================')
    print(f'\t\t\tTotal Weight is : {total_weight}')
    print(f'\t\t\tTotal Profit is : {total_profit}')
    print('===================================================================================')

    return round(total_profit, 2), round(total_weight, 2)


def knapsnack0_1(data_list, W):
    remaining_weight = int(W)
    total_weight = 0
    total_profit = 0

    data_list.sort(key=lambda x: x[2], reverse=True)

    for data in data_list:
        print(data)
        if remaining_weight <= 0:
            break
        if data[0] + total_weight <= W:
            total_weight += data[0]
            remaining_weight -= data[0]
            total_profit += data[1]
        else:
            break

    print('===================================================================================')
    print(f'\t\t\tTotal Weight is : {total_weight}')
    print(f'\t\t\tTotal Profit is : {total_profit}')
    print('===================================================================================')

    return round(total_profit, 2), round(total_weight, 2)


def input_data():
    no_of_inputs = int(input("Enter the Number of enteries : "))
    w = int(input("Enter the size of sack : "))
    data_list = []
    for i in range(no_of_inputs):
        print(f'{i} : ')
        wi = int(input("Enter the Weight : "))
        pi = int(input("Enter the Profit : "))
        ratio = pi/wi
        data = [wi, pi, ratio]
        data_list.append(data)
    return data_list, w
