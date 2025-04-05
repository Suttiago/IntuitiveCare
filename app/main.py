from api.app import app
import os
def main():
    app.run(debug=True,port='8080',host='0.0.0.0')

if __name__ == "__main__":
    main()