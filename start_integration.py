#!/usr/bin/env python3
"""
Simple startup script for IBKR AI Hedge Fund Integration
"""

import os
import sys
import subprocess
import time
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed"""
    required_packages = [
        'ibapi',
        'pandas',
        'schedule',
        'python-dotenv',
        'colorlog',
        'pytz'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("Missing required packages:")
        for package in missing_packages:
            print(f"  - {package}")
        print("\nInstall them with:")
        print(f"pip install {' '.join(missing_packages)}")
        return False
    
    return True

def check_env_file():
    """Check if .env file exists and has required keys"""
    env_file = Path('.env')
    
    if not env_file.exists():
        print("❌ .env file not found")
        print("Please copy env.template to .env and configure your API keys:")
        print("cp env.template .env")
        return False
    
    # Check for required keys
    required_keys = ['OPENAI_API_KEY', 'FINANCIAL_DATASETS_API_KEY']
    missing_keys = []
    
    with open(env_file, 'r') as f:
        content = f.read()
        for key in required_keys:
            if f"{key}=your-" in content or f"{key}=" not in content:
                missing_keys.append(key)
    
    if missing_keys:
        print("❌ Missing required API keys in .env file:")
        for key in missing_keys:
            print(f"  - {key}")
        print("\nPlease edit .env file and add your API keys")
        return False
    
    return True

def check_ai_hedge_fund():
    """Check if AI-Hedge-Fund components are available"""
    if not Path('src').exists():
        print("❌ AI-Hedge-Fund 'src' directory not found")
        print("Please make sure you're in the AI-Hedge-Fund repository root")
        print("Or clone it with: git clone https://github.com/virattt/ai-hedge-fund.git")
        return False
    
    # Check for key files
    required_files = [
        'src/agents/warren_buffett.py',
        'src/agents/valuation.py',
        'src/main.py'
    ]
    
    for file_path in required_files:
        if not Path(file_path).exists():
            print(f"❌ Required file not found: {file_path}")
            return False
    
    return True

def main():
    """Main startup function"""
    print("🚀 IBKR AI Hedge Fund Integration Startup")
    print("=" * 50)
    
    # Check system requirements
    print("1. Checking Python environment...")
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher required")
        sys.exit(1)
    print("✅ Python version OK")
    
    print("\n2. Checking dependencies...")
    if not check_dependencies():
        sys.exit(1)
    print("✅ All dependencies installed")
    
    print("\n3. Checking AI-Hedge-Fund components...")
    if not check_ai_hedge_fund():
        sys.exit(1)
    print("✅ AI-Hedge-Fund components found")
    
    print("\n4. Checking environment configuration...")
    if not check_env_file():
        sys.exit(1)
    print("✅ Environment configuration OK")
    
    print("\n5. Testing configuration...")
    try:
        from config import setup_environment
        config = setup_environment()
        print("✅ Configuration validated")
    except Exception as e:
        print(f"❌ Configuration error: {e}")
        sys.exit(1)
    
    print("\n" + "=" * 50)
    print("✅ All checks passed! Ready to start integration")
    print("=" * 50)
    
    # Ask user if they want to start
    response = input("\nDo you want to start the integration now? (y/n): ")
    if response.lower() in ['y', 'yes']:
        print("\nStarting IBKR AI Hedge Fund Integration...")
        print("Press Ctrl+C to stop")
        print("\nMake sure TWS/IB Gateway is running first!")
        
        # Wait a moment for user to read
        time.sleep(3)
        
        # Start the integration
        try:
            from ibkr_integration import main as integration_main
            integration_main()
        except KeyboardInterrupt:
            print("\n\n👋 Integration stopped by user")
        except Exception as e:
            print(f"\n❌ Error starting integration: {e}")
    else:
        print("\n📋 To start manually, run:")
        print("python ibkr_integration.py")
        print("\nMake sure TWS/IB Gateway is running first!")

if __name__ == "__main__":
    main() 