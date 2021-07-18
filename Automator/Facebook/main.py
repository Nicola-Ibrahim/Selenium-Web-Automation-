from Automator.Facebook.facebook import Facebook
from Automator.WebAutomation import splitting
import pandas as pd
import threading
import os

def facebookMain():
        
    # Read accounts file
    accounts_file_path = os.path.join(os.path.dirname(__file__), "Facebook Accounts.xlsx")
    accounts_data = pd.read_excel(accounts_file_path, usecols=['Email','Email password','Full name','Facebook password','Gender','Profile path','Number of friends','Account status','Creator name', 'group'])


    profile_path = """any profile path"""
    post_path = """https://www.facebook.com/permalink.php?story_fbid=2926945127578775&id=2150524478554181"""
    page_path = """any page path"""


    # Number of threads to be run
    threads = []
    NUM_OF_WORKERS = 1
    groups_items_df = splitting(accounts_data, NUM_OF_WORKERS)

    # Creating threads
    for i in range(NUM_OF_WORKERS):

        # t = threading.Thread(target=Facebook("https://www.facebook.com/").countNFreindsWorker(accounts_file_path, groups_items_df[i][54:55]))
        # t = threading.Thread(target=Facebook("https://www.facebook.com/").checkAccountsWorker(accounts_file_path, groups_items_df[i][67:68]))
        # t = threading.Thread(target=Facebook(accounts_file_path).addLike_CommentOnPostWorker(groups_items_df[i][0:3], post_path))
        t = threading.Thread(target=Facebook(accounts_file_path).addMulitplePersonsWorker(groups_items_df[i], method='all'))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()

