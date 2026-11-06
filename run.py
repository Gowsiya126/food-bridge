import os
from app import create_app

env = os.getenv('FLASK_ENV', 'default')
app = create_app(env)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', '1') == '1'
    print(f"\n========================================================")
    print(f"  FOOD BRIDGE - Smart Food Waste Management Platform")
    print(f"  Server running on http://127.0.0.1:{port}")
    print(f"  Debug mode: {debug}")
    print(f"========================================================\n")
    app.run(host='0.0.0.0', port=port, debug=debug)

