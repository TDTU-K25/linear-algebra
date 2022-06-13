import scipy.io
import numpy as np

########## Requirements ######


def req1(transactions):
    bestSeller = []
    worstSeller = []
    listProduct = []

    # Get all the products in table transactions
    for i in range(0, len(transactions)):
        for j in range(0, len(transactions[i][1])):
            # Three-dimensional array
            listProduct.append(transactions[i][1][j].strip())

    # Sort list in ascending order
    listProduct = sorted(listProduct)

    # Remove duplicate value in listProduct
    listProductAfterRemoveDuplicate = list(dict.fromkeys(listProduct))

    # Count the number of times that each product is sold
    countTimesAppearInList = []
    for i in range(0, len(listProductAfterRemoveDuplicate)):
        count = 0
        for j in range(0, len(listProduct)):
            if (listProductAfterRemoveDuplicate[i] == listProduct[j]):
                count += 1
        countTimesAppearInList.append(count)

    # Group listProductAfterRemoveDuplicate and countTimesAppearInList
    listProductWithTimeAppear = dict(
        zip(listProductAfterRemoveDuplicate, countTimesAppearInList))

    # Get max and min value from dict
    maxValue = max(listProductWithTimeAppear.values())
    minValue = min(listProductWithTimeAppear.values())

    # Find products which are bestSeller and worstSeller
    for key, value in listProductWithTimeAppear.items():
        if (value == maxValue):
            bestSeller.append(key)
        elif (value == minValue):
            worstSeller.append(key)

    return sorted(bestSeller), sorted(worstSeller)


def req2(products):
    maxQuantity = []
    minQuantity = []

    # Get list of products and the number of products in storage from table products
    listProduct = []
    quantityInStorage = []
    for i in range(0, len(products)):
        listProduct.append(products[i][0].strip())
        # remove spaces after string and cast to int type
        quantityInStorage.append(float(products[i][2].strip()))

    # Group listProduct and quantityInStorage
    listProductsWithTheirQuantity = dict(zip(listProduct, quantityInStorage))

    # Get max and min value from dict
    maxValue = max(listProductsWithTheirQuantity.values())
    minValue = min(listProductsWithTheirQuantity.values())

    # Find products which have maxQuantity and minQuantity
    for key, value in listProductsWithTheirQuantity.items():
        if (value == maxValue):
            maxQuantity.append(key)
        elif (value == minValue):
            minQuantity.append(key)

    return sorted(maxQuantity), sorted(minQuantity)


def req3(transactions, products):
    totalRevenue = 0

    # Get list of product, price and the number of products in storage in table products
    listProduct = []
    listPriceOfProduct = []
    quantityInStorage = []
    for i in range(0, len(products)):
        listProduct.append(products[i][0].strip())
        listPriceOfProduct.append(float(products[i][1].strip()))
        # remove spaces after string and cast to int type
        quantityInStorage.append(float(products[i][2].strip()))

    # Get all the products in table transactions
    listProductInTransactions = []
    for i in range(0, len(transactions)):
        for j in range(0, len(transactions[i][1])):
            listProductInTransactions.append(transactions[i][1][j].strip())

    # Count the number of times that each product is sold
    countTimesAppearInList = []
    for i in range(0, len(listProduct)):
        count = 0
        for j in range(0, len(listProductInTransactions)):
            if (listProduct[i] == listProductInTransactions[j]):
                count += 1
        countTimesAppearInList.append(count)

    # Calculate total revenue
    for i in range(0, len(listProduct)):
        totalRevenue += (countTimesAppearInList[i] * listPriceOfProduct[i])

    return round(totalRevenue, 1)


def req4(transactions, products):
    # Get list of product, price and the number of products in storage in table products
    listProduct = []
    listPriceOfProduct = []
    quantityInStorage = []
    for i in range(0, len(products)):
        listProduct.append(products[i][0].strip())
        listPriceOfProduct.append(float(products[i][1].strip()))
        # remove spaces after string and cast to int type
        quantityInStorage.append(float(products[i][2].strip()))

    # Get all the products in table transactions
    listProductInTransactions = []
    for i in range(0, len(transactions)):
        for j in range(0, len(transactions[i][1])):
            listProductInTransactions.append(transactions[i][1][j].strip())

    # Count the number of times that each product is sold
    countTimesAppearInList = []
    for i in range(0, len(listProduct)):
        count = 0
        for j in range(0, len(listProductInTransactions)):
            if (listProduct[i] == listProductInTransactions[j]):
                count += 1
        countTimesAppearInList.append(count)

    # List of revenue of all products
    listRevenueOfAllProducts = []
    revenueOfEachProduct = 0
    for i in range(0, len(listProduct)):
        revenueOfEachProduct += (
            countTimesAppearInList[i] * listPriceOfProduct[i])
        listRevenueOfAllProducts.append(revenueOfEachProduct)
        # reset value of revenueOfEachProduct to calculate revenue for the next product
        revenueOfEachProduct = 0

    # Group listProduct and listRevenueOfAllProducts
    listProductsWithTheirRevenue = dict(
        zip(listProduct, listRevenueOfAllProducts))

    # Get max value from dict
    maxRevenue = max(listProductsWithTheirRevenue.values())

    # Find product that has max revenue
    listProductsHaveMaxRevenue = []
    for key, value in listProductsWithTheirRevenue.items():
        if (value == maxRevenue):
            listProductsHaveMaxRevenue.append(key)

    return sorted(listProductsHaveMaxRevenue)


def req5(history, k):
    numberOfUsers = len(history)
    if (k > numberOfUsers or k <= 0):
        return []

    # Get list of Users and the number of transactions that each user made in table history
    listUser = []
    listNumberOfTransactionCodesOfEachUser = []
    for i in range(0, len(history)):
        listUser.append(history[i][0][0].strip())
        listNumberOfTransactionCodesOfEachUser.append(len(history[i][1]))

    # Group listUser and listNumberOfTransactionCodesOfEachUser
    listUserWithNumberOfTransactionsTheyMade = dict(
        zip(listUser, listNumberOfTransactionCodesOfEachUser))

    # Sorted dict by values in descending order
    listUserWithNumberOfTransactionsTheyMade = dict(sorted(
        listUserWithNumberOfTransactionsTheyMade.items(), key=lambda x: x[1], reverse=True))

    # Convert dict_keys of listUserWithNumberOfTransactionsTheyMade to list
    listUserMadeLotsOfTransactions = list(
        listUserWithNumberOfTransactionsTheyMade.keys())

    return listUserMadeLotsOfTransactions[0:k]  # [0, k - 1]


def req6(transactions, history, k):
    # Get list of Users and transaction codes of each user in table history
    listUser = []
    listTransactionCodesOfEachUser = []
    for i in range(0, len(history)):
        listUser.append(history[i][0][0].strip())
        listTransactionCodesOfEachUser.append(history[i][1])

    # Check whether user k exist in listUser or not
    flag = False
    for user in listUser:
        if (user == k):
            flag = True
    if(flag == False):
        return []

    # Group listUser with listTransactionCodesOfEachUser
    listUserWithTheirTransactionCodes = dict(
        zip(listUser, listTransactionCodesOfEachUser))

    # Get transactions code of user k
    transactionCodesOfUserK = []
    for key in listUserWithTheirTransactionCodes.keys():
        if (key == k):
            temp = listUserWithTheirTransactionCodes.get(key)  # array
            for i in range(0, len(temp)):
                transactionCodesOfUserK.append(temp[i].strip())

    # Get list of transaction codes and all products in each transaction code in table transactions
    listTransactionCode = []
    listProductOfEachTransactionCode = []
    for i in range(0, len(transactions)):
        listProductOfEachTransactionCode.append(transactions[i][1])
        for j in range(0, len(transactions[i][0])):
            listTransactionCode.append(transactions[i][0][j].strip())

    # Group listTransactionCode with listProductOfEachTransactionCode
    listTransactionCodesWithTheirProduct = dict(
        zip(listTransactionCode, listProductOfEachTransactionCode))

    # Get list of product that user k bought
    listProductUserKBought = []
    for key in listTransactionCodesWithTheirProduct.keys():
        for transactionCode in transactionCodesOfUserK:
            if (key == transactionCode):
                temp = listTransactionCodesWithTheirProduct.get(key)  # array
                for i in range(0, len(temp)):
                    listProductUserKBought.append(temp[i])

    # Remove duplicate value in listProductUserKBought
    listProductUserKBoughtRemoveDuplicateValue = list(
        dict.fromkeys(listProductUserKBought))

    # Sort list in ascending order
    listProductUserKBoughtRemoveDuplicateValue = sorted(
        listProductUserKBoughtRemoveDuplicateValue)

    # Get the number of items of each product that K bought
    numberOfItemsOfEachProductKBought = []
    count = 0
    for i in range(0, len(listProductUserKBoughtRemoveDuplicateValue)):
        count = 0
        for j in range(0, len(listProductUserKBought)):
            if (listProductUserKBoughtRemoveDuplicateValue[i] == listProductUserKBought[j]):
                count += 1
        numberOfItemsOfEachProductKBought.append(count)

    # Group listProductUserKBoughtRemoveDuplicateValue with numberOfItemsOfEachProductKBought
    listProductWithNumberOfItemThatKBought = dict(zip(
        listProductUserKBoughtRemoveDuplicateValue, numberOfItemsOfEachProductKBought))

    # Sorted dict by values in descending order
    listProductThatKBoughtMost = dict(sorted(
        listProductWithNumberOfItemThatKBought.items(), key=lambda x: x[1], reverse=True))

    # Get max value from dict
    maxValue = max(listProductThatKBoughtMost.values())

    result = []
    for key, value in listProductThatKBoughtMost.items():
        if (value == maxValue):
            result.append(key)

    return sorted(result)


def req7(transactions, history):
    # Get list of Users, transaction codes and number of transaction codes of each user in table history
    listUser = []
    listTransactionCodesOfEachUser = []
    listNumberOfTransactionCodesOfEachUser = []
    for i in range(0, len(history)):
        listUser.append(history[i][0][0].strip())
        listTransactionCodesOfEachUser.append(history[i][1])
        listNumberOfTransactionCodesOfEachUser.append(len(history[i][1]))

    # Group listUser with listNumberOfTransactionCodesOfEachUser
    listUserWithListNumberOfTransactionCodesOfEachUser = dict(
        zip(listUser, listNumberOfTransactionCodesOfEachUser))

    # Sorted dict by values in descending order
    listUserWithListNumberOfTransactionCodesOfEachUserInDescendingOrder = dict(sorted(
        listUserWithListNumberOfTransactionCodesOfEachUser.items(), key=lambda x: x[1], reverse=True))

    # Find the min value of number of transaction codes of all user
    minNumberOfTransactionCodes = min(
        listUserWithListNumberOfTransactionCodesOfEachUserInDescendingOrder.values())

    # Get all the transaction codes and all the products in each transaction code in table transactions
    listTransactionCodes = []
    listProductInEachTransactionCode = []
    for i in range(0, len(transactions)):
        listProductInEachTransactionCode.append(transactions[i][1])
        for j in range(0, len(transactions[i][0])):
            listTransactionCodes.append(transactions[i][0][j].strip())

    # Group listTransactionCodes with listProductInEachTransactionCode
    listTransactionCodesWithListProductInEachOfThem = dict(
        zip(listTransactionCodes, listProductInEachTransactionCode))

    # Get list of products which all users bought
    listProductAllUserBought = []
    for i in range(0, len(listTransactionCodesOfEachUser)):
        for j in range(0, len(listTransactionCodesOfEachUser[i])):
            for key in listTransactionCodesWithListProductInEachOfThem.keys():
                # remove space after string
                if (key == listTransactionCodesOfEachUser[i][j].strip()):
                    temp = listTransactionCodesWithListProductInEachOfThem.get(
                        key)
                    listProductAllUserBought.append(temp)

    # Group listUser with empty listProductOfEachUser
    listProductOfEachUser = []
    for i in range(0, len(listUser)):
        listProductOfEachUser.append([])
    listUserWithListProductOfEachUser = dict(
        zip(listUser, listProductOfEachUser))

    # Get listProductOfEachUser from listProductAllUserBought
    # listProductAllUserBought in order of all users transaction codes
    j = 0  # The loop variable used to get a number of the transaction codes from listTransactionCodesOfEachUser => How many transactions a user has, how many iterations there are
    k = 0  # The loop variable used to get each element in listProductAllUserBought

    for key in listUserWithListProductOfEachUser.keys():

        for i in range(0, len(listTransactionCodesOfEachUser[j])):
            listUserWithListProductOfEachUser.get(
                key).append(listProductAllUserBought[k])
            k += 1

        j += 1

    # Get listProduct which are sold in store
    listProduct = []
    for i in range(0, len(listProductAllUserBought)):
        for j in range(0, len(listProductAllUserBought[i])):
            listProduct.append(listProductAllUserBought[i][j])
    # Remove duplicate value in listProduct
    listProductAfterRemoveDuplicate = list(dict.fromkeys(listProduct))
    # Sort in ascending order
    listProductAfterRemoveDuplicate = sorted(listProductAfterRemoveDuplicate)

    # Count number of all items each user bought
    numberOfItemsEachUserBought = []
    countNumberOfItems = 0
    for key in listUserWithListProductOfEachUser.keys():
        temp = listUserWithListProductOfEachUser.get(key)
        countNumberOfItems = 0
        for i in range(0, len(temp)):
            countNumberOfItems += len(temp[i])
        numberOfItemsEachUserBought.append(countNumberOfItems)

    # Get list of product which each user bought from multi list into one list
    listProductOfEachUserInOneList = []
    for key in listUserWithListProductOfEachUser.keys():
        temp = listUserWithListProductOfEachUser.get(key)
        for i in range(0, len(temp)):
            tmp = temp[i]
            for j in range(0, len(tmp)):
                listProductOfEachUserInOneList.append(tmp[j])

    # Group listUser with listProductOfEachUserInOneList
    emptyList = []
    for i in range(0, len(listUser)):
        emptyList.append([])
    # initialize (with value of each key is an empty list
    listUserWithlistProductOfEachUserInOneList = dict(zip(listUser, emptyList))

    # Get listUserWithlistProductOfEachUserInOneList from listProductOfEachUserInOneList
    j = 0
    k = 0

    for key in listUserWithlistProductOfEachUserInOneList.keys():

        for i in range(0, numberOfItemsEachUserBought[j]):
            listUserWithlistProductOfEachUserInOneList.get(
                key).append(listProductOfEachUserInOneList[k])
            k += 1

        j += 1

    # Get listProductOfEachUserAfterCombineAllProductInAllTransactionCodesOfThatUser from listUserWithlistProductOfEachUserInOneList
    listProductOfEachUserAfterCombineAllProductInAllTransactionCodesOfThatUser = []
    for key in listUserWithlistProductOfEachUserInOneList.keys():
        listProductOfEachUserAfterCombineAllProductInAllTransactionCodesOfThatUser.append(
            listUserWithlistProductOfEachUserInOneList.get(key))

    # Group listUser with listProductOfEachUserAfterCombineAllProductInAllTransactionCodesOfThatUser
    listUserWithlistProductOfEachUserAfterCombineAllProductInAllTransactionCodesOfThatUser = dict(
        zip(listUser, listProductOfEachUserAfterCombineAllProductInAllTransactionCodesOfThatUser))

    # Find list user with min transaction codes
    listUserWithMinTransactionCodes = []
    for key in listUserWithListNumberOfTransactionCodesOfEachUserInDescendingOrder.keys():
        if (listUserWithListNumberOfTransactionCodesOfEachUserInDescendingOrder.get(key) == minNumberOfTransactionCodes):
            listUserWithMinTransactionCodes.append(key)

    # Get list product of all user with min number of transaction codes bought
    listProductAllUserWithMinNumberOfTransactionCodesBought = []
    for key in listUserWithlistProductOfEachUserAfterCombineAllProductInAllTransactionCodesOfThatUser.keys():
        for user in listUserWithMinTransactionCodes:
            if (key == user):
                listProductAllUserWithMinNumberOfTransactionCodesBought.append(
                    listUserWithlistProductOfEachUserAfterCombineAllProductInAllTransactionCodesOfThatUser.get(key))

    # Get list product of all user with min number of transaction codes bought in one list
    listProductAllUserWithMinNumberOfTransactionCodesBoughtInOneList = []
    for i in range(0, len(listProductAllUserWithMinNumberOfTransactionCodesBought)):
        for j in range(0, len(listProductAllUserWithMinNumberOfTransactionCodesBought[i])):
            listProductAllUserWithMinNumberOfTransactionCodesBoughtInOneList.append(
                listProductAllUserWithMinNumberOfTransactionCodesBought[i][j])

    # Get list number of product of all user with min transaction codes bought
    listNumberOfProductAllUserWithMinNumberOfTransactionCodesBought = []
    for product in listProductAfterRemoveDuplicate:
        count = 0
        for i in range(0, len(listProductAllUserWithMinNumberOfTransactionCodesBoughtInOneList)):
            if (product == listProductAllUserWithMinNumberOfTransactionCodesBoughtInOneList[i]):
                count += 1
        listNumberOfProductAllUserWithMinNumberOfTransactionCodesBought.append(
            count)

    # Group listProductAfterRemoveDuplicate with listNumberOfProductAllUserWithMinNumberOfTransactionCodesBought
    listProductAfterRemoveDuplicateWithlistNumberOfProductAllUserWithMinNumberOfTransactionCodesBought = dict(
        zip(listProductAfterRemoveDuplicate, listNumberOfProductAllUserWithMinNumberOfTransactionCodesBought))

    # Find number of products which user with min number of transaction codes bought most
    maxNumberOfProduct = max(
        listProductAfterRemoveDuplicateWithlistNumberOfProductAllUserWithMinNumberOfTransactionCodesBought.values())

    # List product all user with min number of transaction codes bought most
    listProductAllUserWithMinNumberOfTransactionCodesBoughtMost = []
    for key in listProductAfterRemoveDuplicateWithlistNumberOfProductAllUserWithMinNumberOfTransactionCodesBought.keys():
        if (listProductAfterRemoveDuplicateWithlistNumberOfProductAllUserWithMinNumberOfTransactionCodesBought.get(key) == maxNumberOfProduct):
            listProductAllUserWithMinNumberOfTransactionCodesBoughtMost.append(
                key)

    return sorted(listProductAllUserWithMinNumberOfTransactionCodesBoughtMost)


def req8(transactions, history, k):
    # Get list of Users and transaction codes of each user in table history
    listUser = []
    listTransactionCodesOfEachUser = []
    for i in range(0, len(history)):
        listUser.append(history[i][0][0].strip())
        listTransactionCodesOfEachUser.append(history[i][1])

    # Check whether user k exist in listUser or not
    flag = False
    for user in listUser:
        if (user == k):
            flag = True
    if(flag == False):
        return []

    # Get all the transaction codes and all the products in each transaction code in table transactions
    listTransactionCodes = []
    listProductInEachTransactionCode = []
    for i in range(0, len(transactions)):
        listProductInEachTransactionCode.append(transactions[i][1])
        for j in range(0, len(transactions[i][0])):
            listTransactionCodes.append(transactions[i][0][j].strip())

    # Group listTransactionCodes with listProductInEachTransactionCode
    listTransactionCodesWithListProductInEachOfThem = dict(
        zip(listTransactionCodes, listProductInEachTransactionCode))

    # Get list of products which all users bought
    listProductAllUserBought = []
    for i in range(0, len(listTransactionCodesOfEachUser)):
        for j in range(0, len(listTransactionCodesOfEachUser[i])):
            for key in listTransactionCodesWithListProductInEachOfThem.keys():
                # remove space after string
                if (key == listTransactionCodesOfEachUser[i][j].strip()):
                    temp = listTransactionCodesWithListProductInEachOfThem.get(
                        key)
                    listProductAllUserBought.append(temp)

    # Group listUser with empty listProductOfEachUser
    listProductOfEachUser = []
    for i in range(0, len(listUser)):
        listProductOfEachUser.append([])
    listUserWithListProductOfEachUser = dict(
        zip(listUser, listProductOfEachUser))

    # Get listProductOfEachUser from listProductAllUserBought
    # listProductAllUserBought in order of all users transaction codes
    j = 0  # The loop variable used to get a number of the transaction codes from listTransactionCodesOfEachUser => How many transactions a user has, how many iterations there are
    l = 0  # The loop variable used to get each element in listProductAllUserBought

    for key in listUserWithListProductOfEachUser.keys():

        for i in range(0, len(listTransactionCodesOfEachUser[j])):
            listUserWithListProductOfEachUser.get(
                key).append(listProductAllUserBought[l])
            l += 1

        j += 1

    # Get listProduct which are sold in store
    listProduct = []
    for i in range(0, len(listProductAllUserBought)):
        for j in range(0, len(listProductAllUserBought[i])):
            listProduct.append(listProductAllUserBought[i][j])
    # Remove duplicate value in listProduct
    listProductAfterRemoveDuplicate = list(dict.fromkeys(listProduct))
    # Sort in ascending order
    listProductAfterRemoveDuplicate = sorted(listProductAfterRemoveDuplicate)

    # Count number of all items each user bought
    numberOfItemsEachUserBought = []
    countNumberOfItems = 0
    for key in listUserWithListProductOfEachUser.keys():
        temp = listUserWithListProductOfEachUser.get(key)
        countNumberOfItems = 0
        for i in range(0, len(temp)):
            countNumberOfItems += len(temp[i])
        numberOfItemsEachUserBought.append(countNumberOfItems)

    # Get list of product which each user bought from multi list into one list
    listProductOfEachUserInOneList = []
    for key in listUserWithListProductOfEachUser.keys():
        temp = listUserWithListProductOfEachUser.get(key)
        for i in range(0, len(temp)):
            tmp = temp[i]
            for j in range(0, len(tmp)):
                listProductOfEachUserInOneList.append(tmp[j])

    # Group listUser with listProductOfEachUserInOneList
    emptyList = []
    for i in range(0, len(listUser)):
        emptyList.append([])
    # initialize (with value of each key is an empty list
    listUserWithlistProductOfEachUserInOneList = dict(zip(listUser, emptyList))

    # Get listUserWithlistProductOfEachUserInOneList from listAllProductsInOneList
    j = 0
    l = 0

    for key in listUserWithlistProductOfEachUserInOneList.keys():

        for i in range(0, numberOfItemsEachUserBought[j]):
            listUserWithlistProductOfEachUserInOneList.get(
                key).append(listProductOfEachUserInOneList[l])
            l += 1

        j += 1

    # Get listProductOfEachUserAfterCombineAllProductInAllTransactionCodesOfThatUser from listUserWithlistProductOfEachUserInOneList
    listProductOfEachUserAfterCombineAllProductInAllTransactionCodesOfThatUser = []
    for key in listUserWithlistProductOfEachUserInOneList.keys():
        listProductOfEachUserAfterCombineAllProductInAllTransactionCodesOfThatUser.append(
            listUserWithlistProductOfEachUserInOneList.get(key))

    # Check if user bought that product
    def doesUserBoughtThatProduct(product, listProductUserBought):
        for i in range(0, len(listProductUserBought)):
            if (product == listProductUserBought[i]):
                return True
        return False

    # Count the number of item of  each product all user bought
    listNumberOfItemOfEachProductAllUserBought = []
    # loop through each array containing the products which all users have bought
    for i in range(0, len(listProductOfEachUserAfterCombineAllProductInAllTransactionCodesOfThatUser)):
        # loop through each product the shop sells
        for j in range(0, len(listProductAfterRemoveDuplicate)):
            count = 0
            # Check whether the user has bought that product in the shop or not
            if(doesUserBoughtThatProduct(listProductAfterRemoveDuplicate[j], listProductOfEachUserAfterCombineAllProductInAllTransactionCodesOfThatUser[i])):
                # loop through each product which user bought
                for l in range(0, len(listProductOfEachUserAfterCombineAllProductInAllTransactionCodesOfThatUser[i])):
                    if (listProductAfterRemoveDuplicate[j] == listProductOfEachUserAfterCombineAllProductInAllTransactionCodesOfThatUser[i][l]):
                        count += 1
                listNumberOfItemOfEachProductAllUserBought.append(count)
            else:
                listNumberOfItemOfEachProductAllUserBought.append(count)
                continue  # ignore products that are not in the list of purchased products by user

    # Group listUser with empty listNumberOfItemOfEachProductOfEachUser
    emptyList = []
    for i in range(0, len(listUser)):
        emptyList.append([])
    listUserWithListNumberOfItemOfEachProductOfEachUser = dict(
        zip(listUser, emptyList))

    # Get listNumberOfItemOfEachProductOfEachUser for each user
    l = 0
    for key in listUserWithListNumberOfItemOfEachProductOfEachUser.keys():
        for i in range(0, len(listProductAfterRemoveDuplicate)):
            listUserWithListNumberOfItemOfEachProductOfEachUser.get(
                key).append(listNumberOfItemOfEachProductAllUserBought[l])
            l += 1

    # Get the number of item of each product user k bought
    listNumberOfItemOfEachProductUserKBought = []
    for key in listUserWithListNumberOfItemOfEachProductOfEachUser.keys():
        if (key == k):
            listNumberOfItemOfEachProductUserKBought = listUserWithListNumberOfItemOfEachProductOfEachUser.get(
                key)

    # Calculate Cosine Similarity
    def cosineSimilarity(A, B):
        return np.dot(A, B) / (np.linalg.norm(A) * np.linalg.norm(B))

    # List user with list number of item of each product of each user except user k
    listUserWithListNumberOfItemOfEachProductOfEachUser.pop(k)

    # Find cosine similarity between all user and user k (except user k and user k) then store into a list
    listCosineSimilarityOfUserKtWithEachUser = []
    for key in listUserWithListNumberOfItemOfEachProductOfEachUser.keys():
        listCosineSimilarityOfUserKtWithEachUser.append(cosineSimilarity(
            listNumberOfItemOfEachProductUserKBought, listUserWithListNumberOfItemOfEachProductOfEachUser.get(key)))

    # The most similar
    maxCosineSimilarity = max(listCosineSimilarityOfUserKtWithEachUser)

    # Find the user that bought the same number of item of each product with user k most
    listUserBoughtTheSameNumberOfItemOfEachProductWithUserKMost = []
    for key in listUserWithListNumberOfItemOfEachProductOfEachUser.keys():
        if (maxCosineSimilarity == cosineSimilarity(listNumberOfItemOfEachProductUserKBought, listUserWithListNumberOfItemOfEachProductOfEachUser.get(key))):
            listUserBoughtTheSameNumberOfItemOfEachProductWithUserKMost.append(
                key)

    return sorted(listUserBoughtTheSameNumberOfItemOfEachProductWithUserKMost)


def req9(transactions, history, products):
    # Get list of products and price of them in table product
    listProduct = []
    listPriceOfProduct = []
    for i in range(0, len(products)):
        listProduct.append(products[i][0].strip())
        # remove spaces after string and cast to float type
        listPriceOfProduct.append(float(products[i][1].strip()))

    # Get all the products in table transactions
    listProductInTransactions = []
    for i in range(0, len(transactions)):
        for j in range(0, len(transactions[i][1])):
            listProductInTransactions.append(transactions[i][1][j].strip())

    # Count the number of times that each product is sold
    countTimesAppearInList = []
    for i in range(0, len(listProduct)):
        count = 0
        for j in range(0, len(listProductInTransactions)):
            if (listProduct[i] == listProductInTransactions[j]):
                count += 1
        countTimesAppearInList.append(count)

    # Group listProduct with countTimesAppearInList
    listProductWithNumberOfItemWereSold = dict(
        zip(listProduct, countTimesAppearInList))

    # Find product hasn't been sold
    result = []
    for key, value in listProductWithNumberOfItemWereSold.items():
        if (value == 0):
            result.append(key)

    return sorted(result)


def req10(history, transactions, products, k):
    # Get list of product in store and type of each product in table products
    listProductInStore = []
    listTypeOfEachProduct = []
    for i in range(0, len(products)):
        listProductInStore.append(products[i][0].strip())
        listTypeOfEachProduct.append(int(products[i][3].strip()))

    # Get list of users and transaction codes of each user in table history
    listUser = []
    listTransactionCodesOfEachUser = []
    for i in range(0, len(history)):
        listUser.append(history[i][0][0].strip())
        listTransactionCodesOfEachUser.append(history[i][1])

    # Check whether user k exist in listUser or not
    flag = False
    for user in listUser:
        if (user == k):
            flag = True
    if(flag == False):
        return None

    # Get all the transaction codes and all the products in each transaction code in table transactions
    listTransactionCodes = []
    listProductInEachTransactionCode = []
    for i in range(0, len(transactions)):
        listProductInEachTransactionCode.append(transactions[i][1])
        for j in range(0, len(transactions[i][0])):
            listTransactionCodes.append(transactions[i][0][j].strip())

    # Group listTransactionCodes with listProductInEachTransactionCode
    listTransactionCodesWithListProductInEachOfThem = dict(
        zip(listTransactionCodes, listProductInEachTransactionCode))

    # Get list of products which all users bought
    listProductAllUserBought = []
    for i in range(0, len(listTransactionCodesOfEachUser)):
        for j in range(0, len(listTransactionCodesOfEachUser[i])):
            for key in listTransactionCodesWithListProductInEachOfThem.keys():
                # remove space after string
                if (key == listTransactionCodesOfEachUser[i][j].strip()):
                    temp = listTransactionCodesWithListProductInEachOfThem.get(
                        key)
                    listProductAllUserBought.append(temp)

    # Group listUser with empty listProductOfEachUser
    listProductOfEachUser = []
    for i in range(0, len(listUser)):
        listProductOfEachUser.append([])
    listUserWithListProductOfEachUser = dict(
        zip(listUser, listProductOfEachUser))

    # Get listProductOfEachUser from listProductAllUserBought
    # listProductAllUserBought in order of all users transaction codes
    j = 0  # The loop variable used to get a number of the transaction codes from listTransactionCodesOfEachUser => How many transactions a user has, how many iterations there are
    l = 0  # The loop variable used to get each element in listProductAllUserBought

    for key in listUserWithListProductOfEachUser.keys():

        for i in range(0, len(listTransactionCodesOfEachUser[j])):
            listUserWithListProductOfEachUser.get(
                key).append(listProductAllUserBought[l])
            l += 1

        j += 1

    # Get listProduct which are sold in store
    listProduct = []
    for i in range(0, len(listProductAllUserBought)):
        for j in range(0, len(listProductAllUserBought[i])):
            listProduct.append(listProductAllUserBought[i][j])
    # Remove duplicate value in listProduct
    listProductAfterRemoveDuplicate = list(dict.fromkeys(listProduct))
    # Sort in ascending order
    listProductAfterRemoveDuplicate = sorted(listProductAfterRemoveDuplicate)

    # Count number of all items each user bought
    numberOfItemsEachUserBought = []
    for key in listUserWithListProductOfEachUser.keys():
        temp = listUserWithListProductOfEachUser.get(key)
        countNumberOfItems = 0
        for i in range(0, len(temp)):
            countNumberOfItems += len(temp[i])
        numberOfItemsEachUserBought.append(countNumberOfItems)

    # Get list of product which each user bought from multi list into one list
    listProductOfEachUserInOneList = []
    for key in listUserWithListProductOfEachUser.keys():
        temp = listUserWithListProductOfEachUser.get(key)
        for i in range(0, len(temp)):
            tmp = temp[i]
            for j in range(0, len(tmp)):
                listProductOfEachUserInOneList.append(tmp[j])

    # Group listUser with listProductOfEachUserInOneList
    emptyList = []
    for i in range(0, len(listUser)):
        emptyList.append([])
    # initialize (with value of each key is an empty list
    listUserWithlistProductOfEachUserInOneList = dict(zip(listUser, emptyList))

    # Get listUserWithlistProductOfEachUserInOneList from listProductOfEachUserInOneList
    j = 0
    l = 0

    for key in listUserWithlistProductOfEachUserInOneList.keys():

        for i in range(0, numberOfItemsEachUserBought[j]):
            listUserWithlistProductOfEachUserInOneList.get(
                key).append(listProductOfEachUserInOneList[l])
            l += 1

        j += 1

    # Get listProductOfEachUserAfterCombineAllProductInAllTransactionCodesOfThatUser from listUserWithlistProductOfEachUserInOneList
    listProductOfEachUserAfterCombineAllProductInAllTransactionCodesOfThatUser = []
    for key in listUserWithlistProductOfEachUserInOneList.keys():
        listProductOfEachUserAfterCombineAllProductInAllTransactionCodesOfThatUser.append(
            listUserWithlistProductOfEachUserInOneList.get(key))

    # Group listProductInStore with listTypeOfEachProduct
    listProductInStoreWithListTypeOfEachProduct = dict(
        zip(listProductInStore, listTypeOfEachProduct))

    # Count number of item of all type products of each user bought
    listNumberOfItemOfAllTypesProductOfEachUserBought = []
    for i in range(0, len(listProductOfEachUserAfterCombineAllProductInAllTransactionCodesOfThatUser)):
        countAffordableProduct = 0
        countMidRangeProduct = 0
        countHighEndProduct = 0
        for j in range(0, len(listProductOfEachUserAfterCombineAllProductInAllTransactionCodesOfThatUser[i])):
            if(listProductInStoreWithListTypeOfEachProduct.get(listProductOfEachUserAfterCombineAllProductInAllTransactionCodesOfThatUser[i][j]) == 1):
                countAffordableProduct += 1
            if(listProductInStoreWithListTypeOfEachProduct.get(listProductOfEachUserAfterCombineAllProductInAllTransactionCodesOfThatUser[i][j]) == 2):
                countMidRangeProduct += 1
            if(listProductInStoreWithListTypeOfEachProduct.get(listProductOfEachUserAfterCombineAllProductInAllTransactionCodesOfThatUser[i][j]) == 3):
                countHighEndProduct += 1

        temp = []  # temp list to store number of item of each type of products user bought
        temp.append(countAffordableProduct)
        temp.append(countMidRangeProduct)
        temp.append(countHighEndProduct)

        listNumberOfItemOfAllTypesProductOfEachUserBought.append(temp)

    # Convert list into array and tranverse matrix
    listNumberOfItemOfAllTypesProductOfEachUserBought = np.array(
        listNumberOfItemOfAllTypesProductOfEachUserBought).T

    # Index of User
    listIndexOfUser = []
    for i in range(0, len(listUser)):
        listIndexOfUser.append(i)

    # Group listUser with listIndexOfUser
    listUserWithListIndexOfUser = dict(zip(listUser, listIndexOfUser))

    # Find index of user k
    for key in listUserWithListIndexOfUser.keys():
        if (key == k):
            indexOfUserK = listUserWithListIndexOfUser.get(key)

    # Find max number of item of type of product user k bought most
    maxNumberOfItemOfTypeOfProductUserKBought = listNumberOfItemOfAllTypesProductOfEachUserBought[
        0][indexOfUserK]
    for i in range(1, 3):
        if (maxNumberOfItemOfTypeOfProductUserKBought < listNumberOfItemOfAllTypesProductOfEachUserBought[i][indexOfUserK]):
            maxNumberOfItemOfTypeOfProductUserKBought = listNumberOfItemOfAllTypesProductOfEachUserBought[
                i][indexOfUserK]

    # Find the type of customer
    if (maxNumberOfItemOfTypeOfProductUserKBought == listNumberOfItemOfAllTypesProductOfEachUserBought[0][indexOfUserK] and maxNumberOfItemOfTypeOfProductUserKBought == listNumberOfItemOfAllTypesProductOfEachUserBought[1][indexOfUserK] and maxNumberOfItemOfTypeOfProductUserKBought == listNumberOfItemOfAllTypesProductOfEachUserBought[2][indexOfUserK]):
        typeOfCustomer = 1
    elif (maxNumberOfItemOfTypeOfProductUserKBought == listNumberOfItemOfAllTypesProductOfEachUserBought[0][indexOfUserK] and maxNumberOfItemOfTypeOfProductUserKBought == listNumberOfItemOfAllTypesProductOfEachUserBought[1][indexOfUserK]):
        typeOfCustomer = 1
    elif (maxNumberOfItemOfTypeOfProductUserKBought == listNumberOfItemOfAllTypesProductOfEachUserBought[1][indexOfUserK] and maxNumberOfItemOfTypeOfProductUserKBought == listNumberOfItemOfAllTypesProductOfEachUserBought[2][indexOfUserK]):
        typeOfCustomer = 2
    elif (maxNumberOfItemOfTypeOfProductUserKBought == listNumberOfItemOfAllTypesProductOfEachUserBought[0][indexOfUserK] and maxNumberOfItemOfTypeOfProductUserKBought == listNumberOfItemOfAllTypesProductOfEachUserBought[2][indexOfUserK]):
        typeOfCustomer = 1
    elif (maxNumberOfItemOfTypeOfProductUserKBought == listNumberOfItemOfAllTypesProductOfEachUserBought[0][indexOfUserK]):
        typeOfCustomer = 1
    elif (maxNumberOfItemOfTypeOfProductUserKBought == listNumberOfItemOfAllTypesProductOfEachUserBought[1][indexOfUserK]):
        typeOfCustomer = 2
    elif (maxNumberOfItemOfTypeOfProductUserKBought == listNumberOfItemOfAllTypesProductOfEachUserBought[2][indexOfUserK]):
        typeOfCustomer = 3

    return typeOfCustomer