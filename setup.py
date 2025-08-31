#!/usr/bin/env python3
"""
快速设置脚本
帮助用户配置需求评审自动化工具
"""

import os
import sys

def create_env_file():
    """创建.env配置文件"""
    env_content = """# 模型提供商选择：'openai' 或 'deepseek'
MODEL_PROVIDER=deepseek

# OpenAI 配置
OPENAI_API=your_openai_api_key_here
OPENAI_URL=https://api.openai.com/v1

# DeepSeek 配置
DEEPSEEK_API=your_deepseek_api_key_here
DEEPSEEK_URL=https://api.deepseek.com/v1

# 可选：指定具体模型（如果不设置则使用默认值）
# OPENAI_MODEL=gpt-4o
# DEEPSEEK_MODEL=deepseek-reasoner
"""
    
    if os.path.exists('.env'):
        response = input("📄 .env 文件已存在，是否覆盖？(y/N): ")
        if response.lower() != 'y':
            print("⏭️  跳过 .env 文件创建")
            return False
    
    with open('.env', 'w', encoding='utf-8') as f:
        f.write(env_content)
    print("✅ 已创建 .env 文件")
    return True

def setup_directories():
    """创建必要的目录"""
    directories = ["接口需求集合", "评审结果"]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
            print(f"✅ 已创建目录: {directory}")
        else:
            print(f"ℹ️  目录已存在: {directory}")

def create_sample_data():
    """询问是否创建示例数据"""
    response = input("📊 是否创建示例数据文件？(Y/n): ")
    if response.lower() != 'n':
        try:
            import pandas as pd
            
            # 创建示例需求数据
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
            
            df = pd.DataFrame(data)
            df.to_excel('requirements.xlsx', index=False, engine='openpyxl')
            print("✅ 已创建 requirements.xlsx 示例文件")
            
            # 创建接口示例数据
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
            
            interface_df = pd.DataFrame(interface_data)
            interface_df.to_excel('接口需求集合/CREATE_MUTEX.xlsx', index=False, engine='openpyxl')
            print("✅ 已创建 接口需求集合/CREATE_MUTEX.xlsx 示例文件")
            
        except ImportError:
            print("❌ pandas 未安装，请先运行: pip install pandas openpyxl")
        except Exception as e:
            print(f"❌ 创建示例数据失败: {e}")

def show_next_steps():
    """显示后续步骤"""
    print("\n🎉 设置完成！")
    print("="*50)
    print("📋 接下来的步骤:")
    print("1. 编辑 .env 文件，填入你的 API 密钥")
    print("2. 运行 'python test_config.py' 测试配置")
    print("3. 运行 'python reviewer.py' 进行单个需求评审")
    print("4. 运行 'python reviewer_batch.py' 进行批量评审")
    print("\n💡 提示:")
    print("- 如果使用 DeepSeek，请到 https://platform.deepseek.com 获取 API 密钥")
    print("- 如果使用 OpenAI，请到 https://platform.openai.com 获取 API 密钥")

def main():
    """主函数"""
    print("🚀 需求评审自动化工具 - 快速设置")
    print("="*50)
    
    print("\n📦 Step 1: 创建配置文件")
    create_env_file()
    
    print("\n📁 Step 2: 创建目录结构")
    setup_directories()
    
    print("\n📊 Step 3: 创建示例数据")
    create_sample_data()
    
    show_next_steps()

if __name__ == "__main__":
    main()
