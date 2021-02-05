"""
basic info:
    stereo:    3000, 4
    computer:  2000, 3
    flute:     1500, 1
    phone:     2000, 1
    You can add new items as you want.
"""

class FindBestChoice:
    def __init__(self, weight, price, bag_cap):
        self.item_weight = weight
        self.item_price = price
        self.bag_cap = bag_cap
        # Read the basic info

    def dynamic_programming(self):
        item_num = len(self.item_price)
        cap_num = self.bag_cap
        bag = []  # Store the items in this bag.
        value_matrix = [[0 for _ in range(item_num + 1)] for _ in range(cap_num + 1)]
        # Create a matrix, the columns are items and the rows are 1kg, 2kg, 3kg and 4kg.

        # Try to put the items one by one into 1kg to 4kg capacity bags and record the best choice in the value_matrix.
        for i in range(1, item_num + 1):
            for j in range(1, cap_num + 1):
                if j >= self.item_weight[i - 1]:
                    value_matrix[i][j] = max(
                        value_matrix[i - 1][j],
                        value_matrix[i - 1][j - self.item_weight[i - 1]] + self.item_price[i - 1]
                    )
                    # put this item into the bag if the current capacity is larger than this item.
                else:
                    value_matrix[i][j] = value_matrix[i - 1][j]

        j = cap_num
        for i in range(item_num, 0, -1):
            if value_matrix[i][j] > value_matrix[i - 1][j]:
                bag.append(i - 1)
                j = j - self.item_weight[i - 1]
        return value_matrix[item_num][len(self.item_weight)], bag


if __name__ == '__main__':
    backpack = FindBestChoice([4, 3, 1, 1], [3000, 2000, 1500, 2000], 4)
    print("-------------------------------------------")
    print("Index of the item starts from 0")
    print('Largest value and item index: ', backpack.dynamic_programming())
    print("-------------------------------------------")


