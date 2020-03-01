from localstack.utils.aws import aws_models
MAmcU=super
MAmcS=None
MAmcY=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  MAmcU(LambdaLayer,self).__init__(arn)
  self.cwd=MAmcS
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class RDSDatabase(aws_models.Component):
 def __init__(self,MAmcY,env=MAmcS):
  MAmcU(RDSDatabase,self).__init__(MAmcY,env=env)
 def name(self):
  return self.MAmcY.split(':')[-1]
# Created by pyminifier (https://github.com/liftoff/pyminifier)
