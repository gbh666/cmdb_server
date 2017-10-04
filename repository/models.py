

from django.db import models

class UserProfile(models.Model):
    """
    用户信息
    """
    name = models.CharField(u'姓名', max_length=32)
    email = models.EmailField(u'邮箱')
    phone = models.CharField(u'座机', max_length=32)
    mobile = models.CharField(u'手机', max_length=32)

    class Meta:
        verbose_name_plural = "用户表"

    def __str__(self):
        return self.name


# class Asset(models.Model):
#     """
#     资产信息表，所有资产公共信息（交换机，服务器，防火墙等）
#     """
#     device_type_choices = (
#         (1, '服务器'),
#         (2, '交换机'),
#         (3, '防火墙'),
#     )
#     device_status_choices = (
#         (1, '上架'),
#         (2, '在线'),
#         (3, '离线'),
#         (4, '下架'),
#     )
#
#     device_type_id = models.IntegerField(choices=device_type_choices, default=1)
#     device_status_id = models.IntegerField(choices=device_status_choices, default=1)
#
#     cabinet_num = models.CharField('机柜号', max_length=30, null=True, blank=True)
#     cabinet_order = models.CharField('机柜中序号', max_length=30, null=True, blank=True)
#
#     # idc = models.ForeignKey('IDC', verbose_name='IDC机房', null=True, blank=True)
#     #business_unit = models.ForeignKey('BusinessUnit', verbose_name='属于的业务线', null=True, blank=True)
#
#     #tag = models.ManyToManyField('Tag')
#
#     latest_date = models.DateField(null=True)
#     create_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         verbose_name_plural = "资产表"
#
#     def __str__(self):
#         return "%s-%s-%s" % (self.idc.name , self.cabinet_num, self.cabinet_order)
#
# class NetworkDevice(models.Model):
#     asset = models.OneToOneField('Asset')
#     management_ip = models.CharField('管理IP', max_length=64, blank=True, null=True)
#     vlan_ip = models.CharField('VlanIP', max_length=64, blank=True, null=True)
#     intranet_ip = models.CharField('内网IP', max_length=128, blank=True, null=True)
#     sn = models.CharField('SN号', max_length=64, unique=True)
#     manufacture = models.CharField(verbose_name=u'制造商', max_length=128, null=True, blank=True)
#     model = models.CharField('型号', max_length=128, null=True, blank=True)
#     port_num = models.SmallIntegerField('端口个数', null=True, blank=True)
#     device_detail = models.CharField('设置详细配置', max_length=255, null=True, blank=True)
#
#     class Meta:
#         verbose_name_plural = "网络设备"

class Server(models.Model):
    """
    服务器信息
    """
    # asset = models.OneToOneField('Asset')
    server_status_choices = (
        (1, '上架'),
        (2, '在线'),
        (3, '离线'),
        (4, '下架'),
    )

    server_status_id = models.IntegerField(choices=server_status_choices, default=1)

    hostname = models.CharField(max_length=128, unique=True)
    sn = models.CharField('SN号', max_length=128, db_index=True)
    manufacturer = models.CharField(verbose_name='制造商', max_length=128, null=True, blank=True)
    model = models.CharField('型号', max_length=128, null=True, blank=True)

    manage_ip = models.GenericIPAddressField('管理IP', null=True, blank=True)

    os_platform = models.CharField('系统', max_length=128, null=True, blank=True)
    os_version = models.CharField('系统版本', max_length=128, null=True, blank=True)

    cpu_count = models.IntegerField('CPU个数', null=True, blank=True)
    cpu_physical_count = models.IntegerField('CPU物理个数', null=True, blank=True)
    cpu_model = models.CharField('CPU型号', max_length=128, null=True, blank=True)

    create_at = models.DateTimeField(auto_now_add=True, blank=True)

    latest_date = models.DateTimeField(null=True,blank=True)

    class Meta:
        verbose_name_plural = "服务器表"

    def __str__(self):
        return self.hostname


class Disk(models.Model):
    """
    硬盘信息
    """
    slot = models.CharField('插槽位', max_length=8)
    model = models.CharField('磁盘型号', max_length=32)
    capacity = models.FloatField('磁盘容量GB')
    pd_type = models.CharField('磁盘类型', max_length=32)
    server_obj = models.ForeignKey('Server',related_name='disk')

    class Meta:
        verbose_name_plural = "硬盘表"

    def __str__(self):
        return self.slot


class NIC(models.Model):
    """
    网卡信息
    """
    name = models.CharField('网卡名称', max_length=128)
    hwaddr = models.CharField('网卡mac地址', max_length=64)
    netmask = models.CharField(max_length=64)
    ipaddrs = models.CharField('ip地址', max_length=256)
    up = models.BooleanField(default=False)
    server_obj = models.ForeignKey('Server',related_name='nic')


    class Meta:
        verbose_name_plural = "网卡表"

    def __str__(self):
        return self.name



class Memory(models.Model):
    """
    内存信息
    """
    slot = models.CharField('插槽位', max_length=32)
    manufacturer = models.CharField('制造商', max_length=128, null=True, blank=True)
    model = models.CharField('型号', max_length=128)
    capacity = models.FloatField('容量', null=True, blank=True)
    sn = models.CharField('内存SN号', max_length=128, null=True, blank=True)
    speed = models.CharField('速度', max_length=128, null=True, blank=True)

    server_obj = models.ForeignKey('Server',related_name='memory')


    class Meta:
        verbose_name_plural = "内存表"

    def __str__(self):
        return self.slot

class ServerRecord(models.Model):
    """
    资产变更记录,creator为空时，表示是资产汇报的数据。
    """
    server_obj = models.ForeignKey('Server', related_name='ar')
    content = models.TextField(null=True)
    creator = models.ForeignKey('UserProfile', null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "资产记录表"

    def __str__(self):
        return self.server_obj.hostname


class ErrorLog(models.Model):
    """
    错误日志,如：agent采集数据错误 或 运行错误
    """
    server_obj = models.ForeignKey('Server', null=True, blank=True)
    title = models.CharField(max_length=16)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "错误日志表"

    def __str__(self):
        return self.title

