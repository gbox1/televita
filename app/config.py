import traceback
import json
import sys
import os


try:
    port = int(os.environ.get("PORT", "8080"))
except ValueError:
    port = -1
if not 1 <= port <= 65535:
    print("Please make sure the PORT environment variable is an integer between 1 and 65535")
    sys.exit(1)

try:
    api_id = int(os.environ["API_ID","25528787"])
    api_hash = os.environ["API_HASH","967621d1b0e7003d225526d313e713b"]
except (KeyError, ValueError):
    traceback.print_exc()
    print("\n\nPlease set the API_ID and API_HASH environment variables correctly")
    print("You can get your own API keys at https://my.telegram.org/apps")
    sys.exit(1)

try:
    # index_settings_str = os.environ["INDEX_SETTINGS"].strip()

    # index_settings = json.loads(index_settings_str)

    index_settings = {
      "index_all": False,
      "index_private":True,
      "index_group": True,
      "index_channel": True,
      "exclude_chats": [],
      "include_chats": [int(os.environ["INDEXING_CHAT"])],#my index chat
      "otg": {
          "enable": True,
          "include_private": True,
          "include_group": True,
          "include_channel": True
      }
    }
    otg_settings = index_settings['otg']
    enable_otg = otg_settings['enable']
except:
    traceback.print_exc()
    print("\n\nPlease set the INDEX_SETTINGS environment variable correctly")
    sys.exit(1)

try:
    session_string = os.environ["SESSION_STRING","1BVtsOMQBu8B-3THzZb8T3mIpRFgZzl7KB4Nl6e0uEXXVTGoSKyHgFow2_8R2czA_FqpXJ33RvBDUpLs-smsVk-tutSmGyoZZhvaMrghGNRhLSLIrSLeWZPla3LHRx8Bq14RU1P21trgCJbX-LYa6AwR_edp1OCVE5MAqet8daJIYhv0j8xTZW2AN46MCshtgTCMpUTrsGKAhAHuKetz6YrkuDbBNFZwM122zpPanvez_4BqGoatb6VQV9YJMSc3oSA7-e8Ia3n5TY72LeMsxAB05IPdEdBiwqglFdm-F-Bdcm3J53ulSh3dsB8jcT7ps_4Sak2GA5vHJ5dEbB3CeYL0_5VUBM08="]
except (KeyError, ValueError):
    traceback.print_exc()
    print("\n\nPlease set the SESSION_STRING environment variable correctly")
    sys.exit(1)

# try:
#     bot_token = os.environ["BOT_TOKEN"]
# except (KeyError, ValueError):
#     traceback.print_exc()
#     print("\n\nPlease set the BOT_TOKEN environment variable correctly")
#     sys.exit(1)



host = os.environ.get("HOST", "0.0.0.0")
debug = bool(os.environ.get("DEBUG"))
chat_ids = []
alias_ids = []
