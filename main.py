#!/usr/bin/env python3
"""
需求评审自动化工具 - 主启动脚本
"""

import os
import sys
import argparse

def check_dependencies():
    """检查依赖包"""
    required_packages = ['pandas', 'openai', 'openpyxl', 'python-dotenv']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ 缺少依赖包: {', '.join(missing_packages)}")
        print(f"请运行: pip install {' '.join(missing_packages)}")
        return False
    return True

def check_config():
    """检查配置"""
    if not os.path.exists('.env'):
        print("❌ .env 配置文件不存在")
        print("请运行: python setup.py 进行初始化设置")
        return False
    return True

def run_single_review():
    """运行单个需求评审"""
    if not os.path.exists('requirements.xlsx'):
        print("❌ requirements.xlsx 文件不存在")
        print("请创建需求文件或运行 'python setup.py' 创建示例文件")
        return
    
    print("🚀 开始单个需求评审...")
    os.system('python reviewer.py')

def run_batch_review():
    """运行批量接口评审"""
    if not os.path.exists('接口需求集合'):
        print("❌ 接口需求集合 目录不存在")
        print("请创建目录并添加接口需求文件，或运行 'python setup.py' 创建示例文件")
        return
    
    files = [f for f in os.listdir('接口需求集合') if f.endswith('.xlsx')]
    if not files:
        print("❌ 接口需求集合 目录中没有Excel文件")
        print("请添加接口需求文件，或运行 'python setup.py' 创建示例文件")
        return
    
    print("🚀 开始批量接口评审...")
    os.system('python reviewer_batch.py')

def test_configuration():
    """测试配置"""
    print("🧪 测试模型配置...")
    os.system('python test_config.py')

def setup_project():
    """设置项目"""
    print("⚙️ 项目初始化设置...")
    os.system('python setup.py')

def show_help():
    """显示帮助信息"""
    help_text = """
🤖 需求评审自动化工具

支持的命令：
  setup     - 初始化项目设置（创建配置文件、目录、示例数据）
  test      - 测试大模型配置是否正确
  single    - 运行单个需求评审
  batch     - 运行批量接口评审
  help      - 显示此帮助信息

使用示例：
  python main.py setup    # 首次使用时运行
  python main.py test     # 测试配置
  python main.py single   # 评审 requirements.xlsx
  python main.py batch    # 评审 接口需求集合/ 下所有文件

配置说明：
1. 编辑 .env 文件设置 API 密钥
2. 支持 OpenAI 和 DeepSeek 模型
3. 通过 MODEL_PROVIDER 环境变量切换模型

更多信息请查看 README.md
"""
    print(help_text)

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='需求评审自动化工具')
    parser.add_argument('command', nargs='?', default='help', 
                       choices=['setup', 'test', 'single', 'batch', 'help'],
                       help='要执行的命令')
    
    args = parser.parse_args()
    
    # 显示工具信息
    print("🤖 需求评审自动化工具 v2.0")
    print("支持 OpenAI & DeepSeek 大模型")
    print("="*40)
    
    if args.command == 'help':
        show_help()
        return
    
    if args.command == 'setup':
        setup_project()
        return
    
    # 其他命令需要检查依赖和配置
    if not check_dependencies():
        return
    
    if not check_config():
        return
    
    if args.command == 'test':
        test_configuration()
    elif args.command == 'single':
        run_single_review()
    elif args.command == 'batch':
        run_batch_review()

if __name__ == "__main__":
    main()
