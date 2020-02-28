from localstack.utils.aws import aws_models
byfID=super
byfIc=None
byfIo=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  byfID(LambdaLayer,self).__init__(arn)
  self.cwd=byfIc
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class RDSDatabase(aws_models.Component):
 def __init__(self,byfIo,env=byfIc):
  byfID(RDSDatabase,self).__init__(byfIo,env=env)
 def name(self):
  return self.byfIo.split(':')[-1]
# Created by pyminifier (https://github.com/liftoff/pyminifier)
