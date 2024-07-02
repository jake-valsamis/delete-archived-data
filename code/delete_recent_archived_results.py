from aind_codeocean_api.codeocean import CodeOceanClient
from aind_codeocean_utils.api_handler import APIHandler
import datetime
import os, sys, argparse


def run(delete_after=30, dry_run=True):
    co_client = CodeOceanClient(domain="https://codeocean.allenneuraldynamics.org/", token=os.environ["CUSTOM_KEY"])
    api_handler = APIHandler(co_client=co_client)

    keep_after = datetime.datetime.now() - datetime.timedelta(days=delete_after)

    assets = api_handler.find_archived_data_assets_to_delete(keep_after=keep_after)

    for i,asset in enumerate(assets):
        created = datetime.datetime.fromtimestamp(asset['created'])        
        print(f"{'(dry-run)' if dry_run else ''} deleting {asset['type']} {asset['name']}, created {created}")
        if not dry_run:
            co_client.delete_data_asset(data_asset_id=asset['id'])

if __name__ == "__main__": 
    argparse = argparse.ArgumentParser()
    argparse.add_argument('--dry-run')
    argparse.add_argument('--delete-after', type=int)
    args = argparse.parse_args()
    
    dry_run = args.dry_run != "off"
    run(delete_after=args.delete_after, dry_run=dry_run)