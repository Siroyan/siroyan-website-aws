#!/usr/bin/env python3

from aws_cdk import (
    core,
    aws_s3 as s3,
    aws_s3_deployment as s3_deploy
)
import os

from siroyan_website.siroyan_website_stack import SiroyanWebsiteStack


app = core.App()
SiroyanWebsiteStack(
    app, "siroyan-website",
    env = {
        "region": os.environ["CDK_DEFAULT_REGION"],
        "account": os.environ["CDK_DEFAULT_ACCOUNT"]
    }
)

app.synth()
