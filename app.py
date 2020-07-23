#!/usr/bin/env python3

from aws_cdk import core

from siroyan_website.siroyan_website_stack import SiroyanWebsiteStack


app = core.App()
SiroyanWebsiteStack(app, "siroyan-website")

app.synth()
