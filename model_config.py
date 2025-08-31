"""
大模型配置管理模块
支持 OpenAI 和 DeepSeek 模型的动态配置
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class ModelConfig:
    """大模型配置类"""
    
    SUPPORTED_PROVIDERS = ['openai', 'deepseek']
    
    # 模型映射配置
    MODEL_MAPPING = {
        'openai': {
            'default_model': 'gpt-4o',
            'alternative_models': ['gpt-4', 'gpt-3.5-turbo'],
            'default_url': 'https://api.openai.com/v1'
        },
        'deepseek': {
            'default_model': 'deepseek-reasoner',
            'alternative_models': ['deepseek-chat', 'deepseek-coder'],
            'default_url': 'https://api.deepseek.com/v1'
        }
    }
    
    def __init__(self):
        self.provider = os.getenv('MODEL_PROVIDER', 'deepseek').lower()
        self.validate_provider()
        
        # 根据提供商设置配置
        if self.provider == 'openai':
            self.api_key = os.getenv('OPENAI_API')
            self.base_url = os.getenv('OPENAI_URL', self.MODEL_MAPPING['openai']['default_url'])
            self.model_name = os.getenv('OPENAI_MODEL', self.MODEL_MAPPING['openai']['default_model'])
        elif self.provider == 'deepseek':
            self.api_key = os.getenv('DEEPSEEK_API')
            self.base_url = os.getenv('DEEPSEEK_URL', self.MODEL_MAPPING['deepseek']['default_url'])
            self.model_name = os.getenv('DEEPSEEK_MODEL', self.MODEL_MAPPING['deepseek']['default_model'])
        
        # 验证API密钥
        if not self.api_key:
            raise ValueError(f"请在.env文件中设置 {self.provider.upper()}_API")
        
        # 初始化客户端
        self.client = OpenAI(
            api_key=self.api_key,
            base_url=self.base_url
        )
    
    def validate_provider(self):
        """验证模型提供商"""
        if self.provider not in self.SUPPORTED_PROVIDERS:
            raise ValueError(f"不支持的模型提供商: {self.provider}。支持的提供商: {', '.join(self.SUPPORTED_PROVIDERS)}")
    
    def get_client(self):
        """获取OpenAI客户端"""
        return self.client
    
    def get_model_name(self):
        """获取模型名称"""
        return self.model_name
    
    def get_provider(self):
        """获取当前提供商"""
        return self.provider
    
    def get_config_info(self):
        """获取配置信息（用于日志）"""
        return {
            'provider': self.provider,
            'model': self.model_name,
            'base_url': self.base_url,
            'api_key_set': bool(self.api_key)
        }

def get_model_config():
    """获取模型配置实例"""
    return ModelConfig()

def review_with_llm(prompt: str, config: ModelConfig = None) -> str:
    """
    使用大语言模型进行评审
    
    Args:
        prompt: 评审提示
        config: 模型配置，如果为None则创建新的配置
    
    Returns:
        评审结果
    """
    if config is None:
        config = get_model_config()
    
    try:
        response = config.client.chat.completions.create(
            model=config.model_name,
            messages=[
                {
                    "role": "system", 
                    "content": "你是一个软件工程专家和适航工程师，专注于DO-178C A级软件标准的合规性评审。你的职责是确保软件需求满足最高安全完整性等级的要求。"
                }, 
                {
                    "role": "user", 
                    "content": prompt
                }
            ],
            stream=False,
            max_tokens=10000,
            temperature=0.7,
        )
        return response.choices[0].message.content if response.choices else "无返回结果"
    except Exception as e:
        return f"Error: {str(e)}"
