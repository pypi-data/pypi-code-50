"""
# SPA + CICD Website Construct

This CDK construct is used to create a static website with a CodePipeline to deploy
from source code on pushes to `master`. The goal of this construct is to be able to
point it at a git repository, give it a url,
and you've got a continuously deployed static website.

# This is a pre-release!

This is a quick first-draft. All the options that will likely need to be added to accomodate a large
number of use-cases are still needed. If you'd like to make requests or help update this construct, please
open an [Issue](https://github.com/mbonig/cicd-spa-website/issues) or a [PR](https://github.com/mbonig/cicd-spa-website/pulls).

## What Gets Created

At the base level, the following will be built:

* An S3 bucket for build artifacts
* An S3 bucket for the website content
* CICD Pipeline - CodePipeline sourced from Github, built using CodeBuild and deployed to an S3 bucket.

If a certificate is supplied or requested:

* An ACM certificate will be provisioned via DNS if requested
* A CloudFront Distribution pointing to the S3 bucket.

## Example

This will create the website, the deployment pipeline, and add a generated certificate (and CloudFront) for HTTPS support.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
CicdSpaWebsite(stack, "public-site",
    url="www.matthewbonig.com",
    github_source={
        "owner": "mbonig",
        "repo": "public_site",
        "oauth_token": SecretValue.secrets_manager("github-oauth-token")
    },
    hosted_zone={
        "hosted_zone_id": "ABCDEFGHIJKLM",
        "zone_name": "matthewbonig.com"
    },
    certificate=True
)
```

## Input Properties

|property|description|example
|---|---|---
|url|The url you'd like your website to be available at. Must be full url and must be controlled by the given HostedZone| www.matthewbonig.com
|githubSource.owner|The Github repository's owner | mbonig
|githubSource.repo|The GH repo name | public_site
|githubSource.branch|An optional branch name. Defaults to 'master'| qa
|githubSource.oauthToken|An ISecret pointing to an oauthToken. | SecretValue.secretsManager('github-oauth-token')
|hostedZone|(Optional) - If provided, used to create DNS Records.
|hostedZone.hostedZoneId|The hostedZone ID for the 'url's domain | ABCDEFGHI
|hostedZone.zoneName|The hostedZone's name | matthewbonig.com
|certificate|(Optional) - If provided, creates a CloudFront Distribution with the given certificate. If 'true' is provided, then a certificate will be generated.| true
|buildSpec|(Optional) - If provided, will override the default BuildSpec in the CodeBuild project. Accepts either a string value (the filename in the source code) or an object. The object is passed to the [BuildSpec.fromObject()](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-codebuild.BuildSpec.html#static-from-wbr-objectvalue). If not provided, see [BuildSpec](#buildspec).|build-prod.yaml

## Design Notes

### Certificates

If a certificate is required to provide HTTPS support then a simple S3 Bucket with website hosting will not work. This construct chooses to put a CloudFront Distribution in front of it when a certificate is required.

If that certificate already exists, it can be supplied as an ICertificate. If not, then it will be created using a [DNSValidatedCertificate](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-certificatemanager.DnsValidatedCertificate.html).

If no certificate is supplied or requested, then the site will be hosted using a public S3 Bucket with Website Hosting enabled. No CloudFront Distribution will be created in that case.

### Github Sources

Github source information is provided through props for the construct.

If you'd like to see support for another type of Source action, please open an [Issue](https://github.com/mbonig/cicd-spa-website/issues) or a [PR](https://github.com/mbonig/cicd-spa-website/pulls).

### BuildSpec

The default buildspec is defined at [DEFAULT_BUILD_SPEC](./lib/cicd_spa_website.ts). It uses a Node v12 runtime, runs an `npm install` and then an `npm run build` and assumes the static deliverables are in the `dist` directory.

You may override the BuildSpec with either your own object or by passing a string which will be interpreted as a filename within the source to use.

## Contributing

Please open Pull Requests and Issues on the [Github Repo](https://github.com/mbonig/cicd-spa-website).

## License

MIT
"""
import abc
import builtins
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

import aws_cdk.aws_certificatemanager
import aws_cdk.aws_cloudfront
import aws_cdk.aws_codebuild
import aws_cdk.aws_codepipeline
import aws_cdk.aws_codepipeline_actions
import aws_cdk.aws_iam
import aws_cdk.aws_lambda
import aws_cdk.aws_route53
import aws_cdk.aws_route53_targets
import aws_cdk.aws_s3
import aws_cdk.core

__jsii_assembly__ = jsii.JSIIAssembly.load("cicd_spa_website", "0.1.0", __name__, "cicd_spa_website@0.1.0.jsii.tgz")


class CicdSpaWebsite(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="cicd_spa_website.CicdSpaWebsite"):
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, github_source: "ReducedGitHubSourceActionProps", url: str, build_spec: typing.Any=None, certificate: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.aws_certificatemanager.ICertificate]]]=None, hosted_zone: typing.Optional[aws_cdk.aws_route53.HostedZoneAttributes]=None, description: typing.Optional[str]=None, env: typing.Optional[aws_cdk.core.Environment]=None, stack_name: typing.Optional[str]=None, tags: typing.Optional[typing.Mapping[str,str]]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param github_source: a limited schema version of GitHubSourceActionProps.
        :param url: The url for the website. e.g. www.fourlittledogs.com
        :param build_spec: -
        :param certificate: A certificate to use, or true if you'd like a DnsValidatedCertificate to be generated If provided, also requires the hostedZone to be provided. If you do not provide a certificate or set this to false, then CloudFormation and the related DNS records will not be created, and the website will be hosted using S3
        :param hosted_zone: The HostedZoneAttributes to use for a HostedZone lookup. This is required if you want the DNS entry and are using Certificate generation (instead of providing your own)
        :param description: A description of the stack. Default: - No description.
        :param env: The AWS environment (account/region) where this stack will be deployed. Default: - The ``default-account`` and ``default-region`` context parameters will be used. If they are undefined, it will not be possible to deploy the stack.
        :param stack_name: Name to deploy the stack with. Default: - Derived from construct path.
        :param tags: Stack tags that will be applied to all the taggable resources and the stack itself. Default: {}
        """
        props = CicdSpaWebsiteProps(github_source=github_source, url=url, build_spec=build_spec, certificate=certificate, hosted_zone=hosted_zone, description=description, env=env, stack_name=stack_name, tags=tags)

        jsii.create(CicdSpaWebsite, self, [scope, id, props])

    @jsii.member(jsii_name="setupBucket")
    def setup_bucket(self) -> None:
        return jsii.invoke(self, "setupBucket", [])

    @jsii.member(jsii_name="setupRoute53")
    def setup_route53(self) -> None:
        return jsii.invoke(self, "setupRoute53", [])

    @builtins.property
    @jsii.member(jsii_name="websiteBucket")
    def website_bucket(self) -> aws_cdk.aws_s3.Bucket:
        return jsii.get(self, "websiteBucket")

    @website_bucket.setter
    def website_bucket(self, value: aws_cdk.aws_s3.Bucket):
        jsii.set(self, "websiteBucket", value)


@jsii.data_type(jsii_type="cicd_spa_website.CicdSpaWebsiteProps", jsii_struct_bases=[aws_cdk.core.StackProps], name_mapping={'description': 'description', 'env': 'env', 'stack_name': 'stackName', 'tags': 'tags', 'github_source': 'githubSource', 'url': 'url', 'build_spec': 'buildSpec', 'certificate': 'certificate', 'hosted_zone': 'hostedZone'})
class CicdSpaWebsiteProps(aws_cdk.core.StackProps):
    def __init__(self, *, description: typing.Optional[str]=None, env: typing.Optional[aws_cdk.core.Environment]=None, stack_name: typing.Optional[str]=None, tags: typing.Optional[typing.Mapping[str,str]]=None, github_source: "ReducedGitHubSourceActionProps", url: str, build_spec: typing.Any=None, certificate: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.aws_certificatemanager.ICertificate]]]=None, hosted_zone: typing.Optional[aws_cdk.aws_route53.HostedZoneAttributes]=None):
        """
        :param description: A description of the stack. Default: - No description.
        :param env: The AWS environment (account/region) where this stack will be deployed. Default: - The ``default-account`` and ``default-region`` context parameters will be used. If they are undefined, it will not be possible to deploy the stack.
        :param stack_name: Name to deploy the stack with. Default: - Derived from construct path.
        :param tags: Stack tags that will be applied to all the taggable resources and the stack itself. Default: {}
        :param github_source: a limited schema version of GitHubSourceActionProps.
        :param url: The url for the website. e.g. www.fourlittledogs.com
        :param build_spec: -
        :param certificate: A certificate to use, or true if you'd like a DnsValidatedCertificate to be generated If provided, also requires the hostedZone to be provided. If you do not provide a certificate or set this to false, then CloudFormation and the related DNS records will not be created, and the website will be hosted using S3
        :param hosted_zone: The HostedZoneAttributes to use for a HostedZone lookup. This is required if you want the DNS entry and are using Certificate generation (instead of providing your own)
        """
        if isinstance(env, dict): env = aws_cdk.core.Environment(**env)
        if isinstance(github_source, dict): github_source = ReducedGitHubSourceActionProps(**github_source)
        if isinstance(hosted_zone, dict): hosted_zone = aws_cdk.aws_route53.HostedZoneAttributes(**hosted_zone)
        self._values = {
            'github_source': github_source,
            'url': url,
        }
        if description is not None: self._values["description"] = description
        if env is not None: self._values["env"] = env
        if stack_name is not None: self._values["stack_name"] = stack_name
        if tags is not None: self._values["tags"] = tags
        if build_spec is not None: self._values["build_spec"] = build_spec
        if certificate is not None: self._values["certificate"] = certificate
        if hosted_zone is not None: self._values["hosted_zone"] = hosted_zone

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """A description of the stack.

        default
        :default: - No description.
        """
        return self._values.get('description')

    @builtins.property
    def env(self) -> typing.Optional[aws_cdk.core.Environment]:
        """The AWS environment (account/region) where this stack will be deployed.

        default
        :default:

        - The ``default-account`` and ``default-region`` context parameters will be
          used. If they are undefined, it will not be possible to deploy the stack.
        """
        return self._values.get('env')

    @builtins.property
    def stack_name(self) -> typing.Optional[str]:
        """Name to deploy the stack with.

        default
        :default: - Derived from construct path.
        """
        return self._values.get('stack_name')

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[str,str]]:
        """Stack tags that will be applied to all the taggable resources and the stack itself.

        default
        :default: {}
        """
        return self._values.get('tags')

    @builtins.property
    def github_source(self) -> "ReducedGitHubSourceActionProps":
        """a limited schema version of GitHubSourceActionProps."""
        return self._values.get('github_source')

    @builtins.property
    def url(self) -> str:
        """The url for the website.

        e.g. www.fourlittledogs.com
        """
        return self._values.get('url')

    @builtins.property
    def build_spec(self) -> typing.Any:
        return self._values.get('build_spec')

    @builtins.property
    def certificate(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.aws_certificatemanager.ICertificate]]]:
        """A certificate to use, or true if you'd like a DnsValidatedCertificate to be generated If provided, also requires the hostedZone to be provided.

        If you do not provide a certificate or set this to false, then CloudFormation and the related DNS records will not be created, and the website will be hosted using S3
        """
        return self._values.get('certificate')

    @builtins.property
    def hosted_zone(self) -> typing.Optional[aws_cdk.aws_route53.HostedZoneAttributes]:
        """The HostedZoneAttributes to use for a HostedZone lookup.

        This is required if you want the DNS entry and are using Certificate generation (instead of providing your own)
        """
        return self._values.get('hosted_zone')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CicdSpaWebsiteProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="cicd_spa_website.ReducedGitHubSourceActionProps", jsii_struct_bases=[], name_mapping={'oauth_token': 'oauthToken', 'owner': 'owner', 'repo': 'repo', 'branch': 'branch'})
class ReducedGitHubSourceActionProps():
    def __init__(self, *, oauth_token: aws_cdk.core.SecretValue, owner: str, repo: str, branch: typing.Optional[str]=None):
        """
        :param oauth_token: A GitHub OAuth token to use for authentication. It is recommended to use a Secrets Manager ``Secret`` to obtain the token: const oauth = cdk.SecretValue.secretsManager('my-github-token'); new GitHubSource(this, 'GitHubAction', { oauthToken: oauth, ... });
        :param owner: The GitHub account/user that owns the repo.
        :param repo: The name of the repo, without the username.
        :param branch: The branch to use. Default: "master"
        """
        self._values = {
            'oauth_token': oauth_token,
            'owner': owner,
            'repo': repo,
        }
        if branch is not None: self._values["branch"] = branch

    @builtins.property
    def oauth_token(self) -> aws_cdk.core.SecretValue:
        """A GitHub OAuth token to use for authentication.

        It is recommended to use a Secrets Manager ``Secret`` to obtain the token:

        const oauth = cdk.SecretValue.secretsManager('my-github-token');
        new GitHubSource(this, 'GitHubAction', { oauthToken: oauth, ... });
        """
        return self._values.get('oauth_token')

    @builtins.property
    def owner(self) -> str:
        """The GitHub account/user that owns the repo."""
        return self._values.get('owner')

    @builtins.property
    def repo(self) -> str:
        """The name of the repo, without the username."""
        return self._values.get('repo')

    @builtins.property
    def branch(self) -> typing.Optional[str]:
        """The branch to use.

        default
        :default: "master"
        """
        return self._values.get('branch')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'ReducedGitHubSourceActionProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["CicdSpaWebsite", "CicdSpaWebsiteProps", "ReducedGitHubSourceActionProps", "__jsii_assembly__"]

publication.publish()
