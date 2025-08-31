import pandas as pd
import os

# 创建示例数据
data = {
    '标识': ['REQ_001', 'REQ_002', 'REQ_003'],
    '标题': ['系统初始化需求', '数据验证需求', '错误处理需求'],
    '版本信息': ['V1.0', 'V1.0', 'V1.0'],
    '需求类型': ['功能需求', '功能需求', '功能需求'],
    '是否派生的需求': ['否', '否', '是'],
    '派生理由': ['', '', '基于系统安全要求派生'],
    '接口原型': ['void init_system()', 'bool validate_data(int data)', 'void handle_error(int error_code)'],
    '需求描述': [
        '系统应在接收到启动信号后的500ms内完成初始化过程',
        '系统应对输入数据进行有效性检查，无效数据应被拒绝',
        '系统应在检测到错误时生成相应的错误代码并记录'
    ],
    '测试建议': [
        '验证系统初始化时间不超过500ms',
        '测试有效和无效数据输入',
        '验证错误代码生成和记录功能'
    ],
    '注释': ['无', '需要考虑边界条件', '错误代码需要标准化'],
    '作者': ['张工', '李工', '王工']
}

# 创建DataFrame
df = pd.DataFrame(data)

# 保存为Excel文件
df.to_excel('requirements.xlsx', index=False, engine='openpyxl')
print("已创建 requirements.xlsx 示例文件")

# 为接口需求集合创建示例文件
interface_data = {
    '标识': ['CREATE_MUTEX_001', 'CREATE_MUTEX_002', 'CREATE_MUTEX_003'],
    '标题': ['互斥锁创建需求', '互斥锁参数验证需求', '互斥锁资源管理需求'],
    '版本信息': ['V1.0', 'V1.0', 'V1.0'],
    '需求类型': ['功能需求', '功能需求', '功能需求'],
    '是否派生的需求': ['否', '是', '是'],
    '派生理由': ['', '基于输入验证要求派生', '基于资源管理要求派生'],
    '接口原型': [
        'int CreateMutex(char* name, int priority)', 
        'int ValidateMutexParams(char* name, int priority)',
        'int ReleaseMutexResource(int mutex_id)'
    ],
    '需求描述': [
        '系统应能够创建具有指定名称和优先级的互斥锁',
        '系统应验证互斥锁创建参数的有效性，包括名称长度和优先级范围',
        '系统应在互斥锁不再使用时自动释放相关资源'
    ],
    '测试建议': [
        '测试不同名称和优先级的互斥锁创建',
        '验证参数边界条件和无效输入处理',
        '验证资源释放和内存管理'
    ],
    '注释': ['支持最多64个字符的名称', '优先级范围1-10', '需要防止内存泄漏'],
    '作者': ['赵工', '钱工', '孙工']
}

# 创建接口需求集合DataFrame
interface_df = pd.DataFrame(interface_data)

# 保存到接口需求集合目录
interface_df.to_excel('接口需求集合/CREATE_MUTEX.xlsx', index=False, engine='openpyxl')
print("已创建 接口需求集合/CREATE_MUTEX.xlsx 示例文件")
