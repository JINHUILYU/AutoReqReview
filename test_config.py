#!/usr/bin/env python3
"""
模型配置测试脚本
用于验证大模型配置是否正确
"""

import os
import sys
from model_config import get_model_config

def test_model_config():
    """测试模型配置"""
    print("🧪 测试大模型配置...")
    print("="*50)
    
    try:
        # 测试配置加载
        config = get_model_config()
        config_info = config.get_config_info()
        
        print(f"✅ 配置加载成功!")
        print(f"📋 配置信息:")
        print(f"   - 提供商: {config_info['provider']}")
        print(f"   - 模型: {config_info['model']}")
        print(f"   - API地址: {config_info['base_url']}")
        print(f"   - API密钥已设置: {config_info['api_key_set']}")
        
        # 测试简单对话
        print(f"\n🤖 测试模型对话...")
        test_prompt = "请简单回答：你是什么模型？"
        
        response = config.client.chat.completions.create(
            model=config.model_name,
            messages=[{"role": "user", "content": test_prompt}],
            max_tokens=100,
            temperature=0.1
        )
        
        if response.choices:
            result = response.choices[0].message.content
            print(f"✅ 模型响应成功!")
            print(f"📝 响应内容: {result[:100]}...")
        else:
            print("❌ 模型无响应")
            return False
            
    except Exception as e:
        print(f"❌ 配置测试失败: {str(e)}")
        print("\n💡 请检查:")
        print("   1. .env 文件是否存在且配置正确")
        print("   2. API密钥是否有效")
        print("   3. 网络连接是否正常")
        print("   4. MODEL_PROVIDER 是否设置为 'openai' 或 'deepseek'")
        return False
    
    print(f"\n🎉 所有测试通过! 配置正常.")
    return True

def show_env_template():
    """显示.env文件模板"""
    print("\n📄 .env 文件配置模板:")
    print("="*50)
    template = """# 模型提供商选择：'openai' 或 'deepseek'
MODEL_PROVIDER=deepseek

# OpenAI 配置
OPENAI_API=your_openai_api_key_here
OPENAI_URL=https://api.openai.com/v1

# DeepSeek 配置  
DEEPSEEK_API=your_deepseek_api_key_here
DEEPSEEK_URL=https://api.deepseek.com/v1

# 可选：指定具体模型（如果不设置则使用默认值）
# OPENAI_MODEL=gpt-4o
# DEEPSEEK_MODEL=deepseek-reasoner"""
    print(template)

if __name__ == "__main__":
    print("🚀 大模型配置测试工具")
    print("="*50)
    
    # 检查.env文件是否存在
    if not os.path.exists('.env'):
        print("⚠️  .env 文件不存在!")
        show_env_template()
        print("\n请创建 .env 文件并配置相应的API密钥")
        sys.exit(1)
    
    # 运行测试
    success = test_model_config()
    
    if not success:
        show_env_template()
        sys.exit(1)
    
    print("\n✨ 配置验证完成，可以开始使用评审工具了!")
