import sys;
sys.path.append('./wish.jar')
from com.espark.adarsh import Wish;

if __name__ == '__main__':
    wishObject = Wish();
    wishObject.welcome();
    wishObject.welcome("adarsh kumar");
