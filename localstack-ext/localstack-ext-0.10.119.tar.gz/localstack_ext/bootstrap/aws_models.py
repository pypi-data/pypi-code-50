from localstack.utils.aws import aws_models
mzlRk=super
mzlRI=None
mzlRY=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  mzlRk(LambdaLayer,self).__init__(arn)
  self.cwd=mzlRI
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class RDSDatabase(aws_models.Component):
 def __init__(self,mzlRY,env=mzlRI):
  mzlRk(RDSDatabase,self).__init__(mzlRY,env=env)
 def name(self):
  return self.mzlRY.split(':')[-1]
# Created by pyminifier (https://github.com/liftoff/pyminifier)
