import sys
import platform
import json

def check_environment():
    # 检查Python版本
    if sys.version_info < (3, 9):
        print("错误: 需要Python 3.9或更高版本")
        return False
    
    # 检查操作系统
    if platform.system() not in ['Linux', 'Darwin']:
        print("警告: 非Linux/macOS系统可能影响性能")
    
    # 检查配置文件
    try:
        with open('cloudstudio_deploy.json') as f:
            config = json.load(f)
            print(f"项目配置加载成功: {config['project_name']}")
    except Exception as e:
        print(f"配置文件错误: {str(e)}")
        return False
    
    return True

if __name__ == "__main__":
    if not check_environment():
        sys.exit(1)
    print("环境检查通过")
    sys.exit(0)