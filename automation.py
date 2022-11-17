import boto3

##ec2 = boto3.client('ec2',
##                     aws_access_key_id='AKIAYCI6QZFEN2H6U6DO',
##                     aws_secret_access_key='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',
##                     region_name='ap-south-1')
##
##'listing the instances_ids'
##instance = ec2.describe_instances()['Reservations']
##instances_list = []
##for ins in instance:
##    instance_id = ins['Instances'][0]['InstanceId']
##    instances_list.append(instance_id)
##print('list of instances:',instances_list)
##
##'creating instance function'
##def instance_create():
##        instance = ec2.run_instances(
##            ImageId='ami-0e6329e222e662a52',
##            MinCount=1,
##            MaxCount=1,
##            InstanceType='t2.micro')
##   
##if len(instances_list) < 2:
##    instance_create()
##
##
##
##'listing the amis'
##ami = ec2.describe_images(Owners=['self'])
##ami_list = []
##for ami_id in ami['Images']:
##    ami_list.append(ami_id['ImageId'])
##print(ami_list)
##
##'creating Image'
##def create_image():
##    ec2.create_image(InstanceId=instances_list[0], Name='auto ami2')
##
##if len(ami_list)<2:
##    create_image()



'lauching configuration'
try:
    autoscaling = boto3.client('autoscaling',
                         aws_access_key_id='AKIAYCI6QZFEN2H6U6DO',
                         aws_secret_access_key='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',
                         region_name='ap-south-1')

    configs = autoscaling.create_launch_configuration(
        LaunchConfigurationName='ec2_instance2',
        ImageId=ami_list[1],
        InstanceType='t2.micro')

except Exception as e:
    print(e)

'listing the launch configurations'
##launch_configs = autoscaling.describe_launch_configurations()
##list_configs = []
##
##for configurations in launch_configs['LaunchConfigurations']:
##    list_configs.append(configurations['LaunchConfigurationName'])
##
##print(list_configs)

    
'creating autoscaling group'
##try:
##    for name in list_configs:
##        autoscale_group = autoscaling.create_auto_scaling_group(
##            AutoScalingGroupName = name+' '+'auto',
##            LaunchConfigurationName = name,
##            AvailabilityZones = ['ap-south-1a'],
##            DesiredCapacity=2,
##            MinSize=1,
##            MaxSize=5,
##            Tags=[{'Key': 'application1'}])
##except Exception as e:
##    print(e)


'listing autoscaling groups'
auto_groups = autoscaling.describe_auto_scaling_groups()['AutoScalingGroups']
auto_scale_list = []

for group in auto_groups:
    auto_scale_list.append(group['AutoScalingGroupName'])

print(auto_scale_list)


'Load Balancing'
load_balancer = boto3.client('elbv2',
                             aws_access_key_id='AKIAYCI6QZFEN2H6U6DO',
                             aws_secret_access_key='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',
                             region_name='ap-south-1')

'creating target groups'
def create_target_group():
    target_group = load_balancer.create_target_group(
        Name = 'target2',
        TargetType='instance',
        Protocol = 'HTTP',
        Port=80,
        HealthCheckPath='/app1',
        VpcId='vpc-00b54c520d17903ee'
        )

'creating load balancer'
def create_load_balancer():
    balancer = load_balancer.create_load_balancer(
        Name='loadbalancer1',
        Subnets=['subnet-01351d724fe53397b','subnet-05dd3292a913d35a3'])


'adding target groups to load balancer'
def add_targets_to_balancer():
    listener = load_balancer.create_listener(
        
        DefaultActions=[{'Type':'forward',
        'Order':1,
        'TargetGroupArn':'arn:aws:elasticloadbalancing:ap-south-1:554651666760:targetgroup/target1/6c6bbdd83fa757c7',
         
         
        'Order':2,'TargetGroupArn':'arn:aws:elasticloadbalancing:ap-south-1:554651666760:targetgroup/target2/2b9c1141ca6a5033',
         }
        ],
        LoadBalancerArn='arn:aws:elasticloadbalancing:ap-south-1:554651666760:loadbalancer/app/loadbalancer1/9642dbde722e8f22',
        Protocol='HTTP',
        Port=80)





















