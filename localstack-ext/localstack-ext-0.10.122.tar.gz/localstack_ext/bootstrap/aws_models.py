from localstack.utils.aws import aws_models
xLNkK=super
xLNku=None
xLNkz=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  xLNkK(LambdaLayer,self).__init__(arn)
  self.cwd=xLNku
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class RDSDatabase(aws_models.Component):
 def __init__(self,xLNkz,env=xLNku):
  xLNkK(RDSDatabase,self).__init__(xLNkz,env=env)
 def name(self):
  return self.xLNkz.split(':')[-1]
# Created by pyminifier (https://github.com/liftoff/pyminifier)
