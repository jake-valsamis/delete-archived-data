import argparse
import datetime
import logging
import os
import sys

from codeocean import CodeOcean
from codeocean.data_asset import DataAssetSearchParams


def find_archived_data_assets_to_delete(client, keep_after):
    data_asset_params = DataAssetSearchParams(
        offset=0,
        limit=1000,
        sort_order="desc",
        type="dataset",
        archived=True,
    )

    data_assets = client.data_assets.search_data_assets_iterator(data_asset_params)

    for d in data_assets:
        created = datetime.datetime.fromtimestamp(d.created)
        last_used = (
            datetime.datetime.fromtimestamp(d.last_used) if d.last_used != 0 else None
        )
        old = created < keep_after
        not_used_recently = not last_used or last_used < keep_after

        if old and not_used_recently:
            yield d, created, last_used


def run(client, keep_after, dry_run):
    assets = find_archived_data_assets_to_delete(client=client, keep_after=keep_after)

    internal_size = 0
    external_size = 0
    total_internal_assets = 0
    total_external_assets = 0

    for asset, created, last_used in assets:
        size = asset.size or 0 
        logging.info(
            f"{'(dry-run)' if dry_run else ''} deleting {asset.type} {asset.name}, created {created}, last_used {last_used}, size {size/1e9} GB"
        )

        print(asset)
        if asset.source_bucket and asset.source_bucket.external:
            external_size += size
            total_external_assets += 1
        else:
            internal_size += size
            total_internal_assets += 1

        if not dry_run:
            client.delete_data_asset(data_asset_id=asset["id"])

    logging.info(f"total external assets: {total_external_assets}")
    logging.info(f"total external size: {external_size/1e9} GB")
    logging.info(f"total internal assets: {total_internal_assets}")
    logging.info(f"total internal size: {internal_size/1e9} GB")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    argparse = argparse.ArgumentParser()
    argparse.add_argument("--dry-run")
    argparse.add_argument("--delete-after", type=int)
    args = argparse.parse_args()

    dry_run = args.dry_run != "off"
    keep_after = datetime.datetime.now() - datetime.timedelta(days=args.delete_after)

    co_client = CodeOcean(
        domain=os.environ["CODE_OCEAN_DOMAIN"],
        token=os.environ["CUSTOM_KEY"],
    )

    run(client=co_client, keep_after=keep_after, dry_run=dry_run)
