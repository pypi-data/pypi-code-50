from localstack.utils.aws import aws_models
irnEU=super
irnEq=None
irnEA=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  irnEU(LambdaLayer,self).__init__(arn)
  self.cwd=irnEq
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class RDSDatabase(aws_models.Component):
 def __init__(self,irnEA,env=irnEq):
  irnEU(RDSDatabase,self).__init__(irnEA,env=env)
 def name(self):
  return self.irnEA.split(':')[-1]
# Created by pyminifier (https://github.com/liftoff/pyminifier)
