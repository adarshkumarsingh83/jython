import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),'./target/wish.jar'))

from com.espark.adarsh import ApplicationWish;

if __name__ == '__main__':
    wishObject = ApplicationWish();
    response = wishObject.getWish();
    print("Default Response "+response);
    response = wishObject.getWish("adarsh kumar");
    print("Argumented Response "+response);