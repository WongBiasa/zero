import os
import sys
import time 
import random

banner1 = (''' 

 /$$$$$$$$                                     /$$$$$$$$                     /$$           /$$   /$$    
|_____ $$                                     | $$_____/                    | $$          |__/  | $$    
     /$$/   /$$$$$$   /$$$$$$   /$$$$$$       | $$       /$$   /$$  /$$$$$$ | $$  /$$$$$$  /$$ /$$$$$$  
    /$$/   /$$__  $$ /$$__  $$ /$$__  $$      | $$$$$   |  $$ /$$/ /$$__  $$| $$ /$$__  $$| $$|_  $$_/  
   /$$/   | $$$$$$$$| $$  \__/| $$  \ $$      | $$__/    \  $$$$/ | $$  \ $$| $$| $$  \ $$| $$  | $$    
  /$$/    | $$_____/| $$      | $$  | $$      | $$        >$$  $$ | $$  | $$| $$| $$  | $$| $$  | $$ /$$
 /$$$$$$$$|  $$$$$$$| $$      |  $$$$$$/      | $$$$$$$$ /$$/\  $$| $$$$$$$/| $$|  $$$$$$/| $$  |  $$$$/
|________/ \_______/|__/       \______/       |________/|__/  \__/| $$____/ |__/ \______/ |__/   \___/  
                                                                  | $$                                  
                                                                  | $$                                  
                                                                  |__/                                  
    .:| Author : Security77 Github:Security77 Twiter: @iAmHere96509046  |:. 
''')

banner2 = ('''

    )                                                    
 ( /(                                   (             )  
 )\())  (   (          (       )        )\     (   ( /(  
((_)\  ))\  )(    (    )\   ( /( `  )  ((_) (  )\  )\()) 
 _((_)/((_)(()\   )\  ((_)  )\())/(/(   _   )\((_)(_))/  
|_  /(_))   ((_) ((_) | __|((_)\((_)_\ | | ((_)(_)| |_   
 / / / -_) | '_|/ _ \ | _| \ \ /| '_ \)| |/ _ \| ||  _|  
/___|\___| |_|  \___/ |___|/_\_\| .__/ |_|\___/|_| \__|  
                                |_|                      
    .:| Author : Security77 Github:Security77 Twiter: @iAmHere96509046  |:. 
''')

banner3 = ('''

 ********                               ********                  **          **   **  
//////**                               /**/////          ******  /**         //   /**  
     **    *****  ******  ******       /**       **   **/**///** /**  ******  ** ******
    **    **///**//**//* **////**      /******* //** ** /**  /** /** **////**/**///**/ 
   **    /******* /** / /**   /**      /**////   //***  /******  /**/**   /**/**  /**  
  **     /**////  /**   /**   /**      /**        **/** /**///   /**/**   /**/**  /**  
 ********//******/***   //******       /******** ** //**/**      ***//****** /**  //** 
////////  ////// ///     //////        //////// //   // //      ///  //////  //    //  
    .:| Author : Security77 Github:Security77 Twiter: @iAmHere96509046  |:.                                                                     

''')


choi = (banner1, banner2, banner3)
print (random.choice(choi))
time.sleep(0.6)

def main():
    print 'ketik "help" untuk mengetahui module.!'
    inpt = raw_input('Zero->>')

    if inpt =='ddos':
        ddos()

    elif inpt == 'ifconfig':
        os.system('ifconfig')
    
    elif inpt == 'sniff':
        sniff()

    elif inpt == 'nmap':
        nmap()

    elif inpt == 'spoff':
        spoff()

    elif inpt == 'exit':
        print '[+]Shutting down.!'
        os.system('exit')

    elif inpt == 'deface':
        deface()

    elif inpt == 'image':
        image()

    elif inpt == 'help':
        help()
    else:
        print '[+]Perintah tidak ditemukan'
        main()

def help():
    print '''
    \t+========================+
    \t|       Perintah         | 
    \t|         sniff          |
    \t|         spoff          | 
    \t|         nmap           |
    \t|         image          | 
    \t|         deface         |
    '''
    main()
def image():
    print 'yo'


main()