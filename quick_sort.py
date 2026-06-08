"""
快速排序算法实现
Quick Sort Algorithm Implementation
"""


def quick_sort(arr):
    """
    使用快速排序算法对数组进行排序
    
    参数:
        arr: 待排序的列表
    
    返回:
        排序后的列表
    
    时间复杂度: 
        平均情况: O(n log n)
        最坏情况: O(n^2)
    
    空间复杂度: O(log n) - 递归栈深度
    """
    if len(arr) <= 1:
        return arr
    
    # 选择第一个元素作为基准
    pivot = arr[0]
    
    # 分割数组
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    
    # 递归排序并合并
    return quick_sort(left) + [pivot] + quick_sort(right)


def quick_sort_inplace(arr, low=0, high=None):
    """
    原地快速排序算法 - 空间效率更高
    
    参数:
        arr: 待排序的列表
        low: 左边界索引
        high: 右边界索引
    
    返回:
        排序后的列表（原地修改）
    
    空间复杂度: O(log n) - 仅递归栈空间
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # 获取分割点
        pivot_index = partition(arr, low, high)
        
        # 递归排序左右两部分
        quick_sort_inplace(arr, low, pivot_index - 1)
        quick_sort_inplace(arr, pivot_index + 1, high)
    
    return arr


def partition(arr, low, high):
    """
    分割函数 - 选择最后一个元素作为基准
    
    参数:
        arr: 数组
        low: 左边界
        high: 右边界
    
    返回:
        基准元素的最终位置
    """
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# 测试代码
if __name__ == "__main__":
    # 测试数据
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [1],
        [],
        [3, 3, 3, 3],
        [5, 4, 3, 2, 1],
    ]
    
    print("快速排序算法测试")
    print("=" * 50)
    
    for arr in test_arrays:
        original = arr.copy()
        sorted_arr = quick_sort(arr)
        print(f"原数组: {original}")
        print(f"排序后: {sorted_arr}")
        print("-" * 50)
    
    print("\n原地快速排序测试")
    print("=" * 50)
    
    for arr in test_arrays:
        original = arr.copy()
        quick_sort_inplace(arr)
        print(f"原数组: {original}")
        print(f"排序后: {arr}")
        print("-" * 50)
