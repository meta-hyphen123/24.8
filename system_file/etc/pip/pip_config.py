import requests
import sys
import json
import subprocess

# 国内镜像源列表
MIRRORS = {
    'default': 'https://pypi.org/pypi',
    'aliyun': 'https://mirrors.aliyun.com/pypi',
    'tencent': 'https://mirrors.cloud.tencent.com/pypi/simple',
    'huawei': 'https://mirrors.huaweicloud.com/repository/pypi/simple',
    'douban': 'https://pypi.douban.com/simple',
    # 添加更多镜像源
}

def get_package_info(package_name, version=None, mirror='default'):
    base_url = MIRRORS.get(mirror, MIRRORS['default'])
    if version:
        url = f"{base_url}/{package_name}/{version}/json"
    else:
        url = f"{base_url}/{package_name}/json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        if response.status_code == 404:
            print(f"Package '{package_name}' not found in mirror '{mirror}'.")
        else:
            print(f"HTTP error occurred: {e}")
        return None
    except requests.RequestException as e:
        print(f"Error fetching package info from {url}: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response from {url}: {e}")
        return None

def install_package(package_name, version=None):
    for mirror in MIRRORS:
        package_info = get_package_info(package_name, version, mirror)
        if package_info:
            urls = package_info.get('urls')
            if urls:
                wheel_url = next((url['url'] for url in urls if url['packagetype'] == 'bdist_wheel'), None)
                if wheel_url:
                    subprocess.run(['pip', 'install', wheel_url])
                    print(f"Successfully installed {package_name} {version} from {mirror}.")
                    return
                else:
                    print(f"No wheel package found for {package_name} {version} in {mirror}.")
            else:
                print(f"No download URLs found for {package_name} {version} in {mirror}.")
        else:
            print(f"Package '{package_name}' not found in mirror '{mirror}'.")

    print(f"Failed to install {package_name} {version} from any of the mirrors.")

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python pip_config.py <package_name> [version]")
        sys.exit(1)

    package_name = sys.argv[1]
    version = sys.argv[2] if len(sys.argv) == 3 else None

    install_package(package_name, version)

if __name__ == "__main__":
    main()
