# 项目描述

## 项目概述

本项目是针对 **JumpServer v3 最新版本** 开发的 **SDK（软件开发工具包）**。JumpServer 是一款开源的堡垒机系统，提供安全、高效的运维审计能力。本
SDK 旨在为开发者提供便捷的接口和工具，以便快速集成 JumpServer v3 的功能，实现自动化运维、资源管理、用户权限控制等操作。

---

## 项目目标

1. **简化集成**：提供简单易用的 API 接口，帮助开发者快速集成 JumpServer v3 的核心功能。
2. **功能覆盖**：支持 JumpServer v3 的主要功能模块，包括用户管理、资产管理、权限控制、会话审计等。
3. **提高效率**：通过 SDK 实现自动化操作，减少手动配置和管理的时间成本。
4. **兼容性与扩展性**：确保 SDK 兼容 JumpServer v3 的最新版本，并提供良好的扩展性，方便后续功能迭代。

---

## SDK 功能特性

目前 SDK 提供下方接口功能封装，使用详情请查看本项目 `tests` 目录下的测试用例。

### 认证

| 请求类型 | 请求名称            | 备注 |
|------|-----------------|----|
| -    | 基于 AccessKey 认证 | -  |
| -    | 基于 账号/密码 认证     | -  |

### 用户管理

| 请求类型         | 请求名称                                     | 备注 |
|--------------|------------------------------------------|----|
| 列表查询         | `DescribeUsersRequest`                   | -  |
| 详情查询         | `DetailUserRequest`                      | -  |
| 创建           | `CreateUserRequest`                      | -  |
| 更新           | `UpdateUserRequest`                      | -  |
| 删除           | `DeleteUserRequest`                      | -  |
| 邀请           | `InviteUserRequest`                      | -  |
| 移除           | `RemoveUserRequest`                      | -  |
| 获取`资产`被授权的用户 | `DescribeAuthorizedUsersForAssetRequest` | -  |

### 用户角色管理

| 请求类型   | 请求名称                           | 备注 |
|--------|--------------------------------|----|
| 列表查询   | `DescribeRolesRequest`         | -  |
| 详情查询   | `DetailRoleRequest`            | -  |
| 创建     | `CreateRoleRequest`            | -  |
| 更新     | `UpdateRoleRequest`            | -  |
| 删除     | `DeleteRoleRequest`            | -  |
| 关联用户查询 | `DescribeUsersWithRoleRequest` | -  |
| 追加用户   | `AppendUsersToRoleRequest`     | -  |
| 移除用户   | `DescribeUsersWithRoleRequest` | -  |

### 用户组管理

| 请求类型   | 请求名称                          | 备注 |
|--------|-------------------------------|----|
| 列表查询   | `DescribeUserGroupsRequest`   | -  |
| 详情查询   | `DetailUserGroupRequest`      | -  |
| 创建     | `CreateUserGroupRequest`      | -  |
| 更新     | `UpdateUserGroupRequest`      | -  |
| 删除     | `DeleteUserGroupRequest`      | -  |
| 追加用户   | `AppendUserToGroupRequest`    | -  |
| 追加全部用户 | `AppendAllUserToGroupRequest` | -  |
| 移除用户   | `RemoveUserFromGroupRequest`  | -  |

### 资产管理

| 请求类型 | 请求名称                     | 备注                                                           |
|------|--------------------------|--------------------------------------------------------------|
| 列表查询 | `DescribeAssetsRequest`  | 可按照分类查询，Asset 可更换为 Host/Database/Cloud/Device/Web/GPT/Custom |
| 详情查询 | `DetailAssetRequest`     | 可按照分类查询，同上                                                   |
| 创建   | `CreateHostRequest`      | 只可按照具体分类查询，Host 可更换为 Database/Cloud/Device/Web/GPT/Custom    |
| 更新   | `UpdateHostRequest`      | 只可按照具体分类查询，同上                                                |
| 删除   | `DeleteAssetRequest`     | -                                                            |
| 批量删除 | `BulkDeleteAssetRequest` | -                                                            |

### 平台管理

| 请求类型    | 请求名称                           | 备注 |
|---------|--------------------------------|----|
| 列表查询    | `DescribePlatformsRequest`     | -  |
| 详情查询    | `DetailPlatformRequest`        | -  |
| 创建      | `CreatePlatformRequest`        | -  |
| 更新      | `UpdatePlatformRequest`        | -  |
| 删除      | `DeletePlatformRequest`        | -  |
| 同步协议到资产 | `SyncProtocolsToAssetsRequest` | -  |

### 网域管理

| 请求类型 | 请求名称                     | 备注 |
|------|--------------------------|----|
| 列表查询 | `DescribeDomainsRequest` | -  |
| 详情查询 | `DetailDomainRequest`    | -  |
| 创建   | `CreateDomainRequest`    | -  |
| 更新   | `UpdateDomainRequest`    | -  |
| 删除   | `DeleteDomainRequest`    | -  |

### 节点管理

| 请求类型 | 请求名称                   | 备注 |
|------|------------------------|----|
| 列表查询 | `DescribeNodesRequest` | -  |
| 详情查询 | `DetailNodeRequest`    | -  |
| 创建   | `CreateNodeRequest`    | -  |
| 更新   | `CreateNodeRequest`    | -  |
| 删除   | `DeleteNodeRequest`    | -  |

### 组织管理

| 请求类型 | 请求名称                           | 备注 |
|------|--------------------------------|----|
| 列表查询 | `DescribeOrganizationsRequest` | -  |
| 详情查询 | `DetailOrganizationRequest`    | -  |
| 创建   | `CreateOrganizationRequest`    | -  |
| 更新   | `UpdateOrganizationRequest`    | -  |
| 删除   | `DeleteOrganizationRequest`    | -  |

### 权限管理

| 请求类型            | 请求名称                                       | 备注                              |
|-----------------|--------------------------------------------|---------------------------------|
| 列表查询            | `DescribePermissionsRequest`               | -                               |
| 详情查询            | `DetailPermissionRequest`                  | -                               |
| 创建              | `CreatePermissionRequest`                  | -                               |
| 更新              | `UpdatePermissionRequest`                  | -                               |
| 删除              | `DeletePermissionRequest`                  | -                               |
| 查询`用户和资产`对应的授权  | `DescribePermsForAssetAndUserRequest`      | DescribePermissionsRequest 也可实现 |
| 查询`用户组和资产`对应的授权 | `DescribePermsForAssetAndUserGroupRequest` | DescribePermissionsRequest 也可实现 |

### 审计管理

| 请求类型        | 请求名称                                | 备注 |
|-------------|-------------------------------------|----|
| 在线用户查询 - 列表 | `DescribeUserSessionsRequest`       | -  |
| 在线用户查询 - 详情 | `DetailUserSessionRequest`          | -  |
| 登录日志 - 列表   | `DescribeLoginLogsRequest`          | -  |
| 登录日志 - 详情   | `DetailLoginLogRequest`             | -  |
| 操作日志 - 列表   | `DescribeOperateLogsRequest`        | -  |
| 操作日志 - 详情   | `DetailOperateLogRequest`           | -  |
| 用户改密日志 - 列表 | `DescribeChangePasswordLogsRequest` | -  |
| 用户改密日志 - 详情 | `DetailChangePasswordLogRequest`    | -  |
| 作业日志 - 列表   | `DescribeJobLogsRequest`            | -  |
| 作业日志 - 详情   | `DetailJobLogRequest`               | -  |
| FTP 记录 - 列表 | `DescribeFTPLogsRequest`            | -  |
| FTP 记录 - 详情 | `DetailFTPLogRequest`               | -  |
| 会话记录 - 列表   | `DescribeSessionsRequest`           | -  |
| 会话记录 - 详情   | `DetailSessionRequest`              | -  |
| 命令记录 - 列表   | `DescribeCommandsRequest`           | -  |
| 命令记录 - 详情   | `DetailCommandRequest`              | -  |

### 标签管理

| 请求类型 | 请求名称                    | 备注 |
|------|-------------------------|----|
| 列表查询 | `DescribeLabelsRequest` | -  |
| 详情查询 | `DetailLabelRequest`    | -  |
| 创建   | `CreateLabelRequest`    | -  |
| 更新   | `UpdateLabelRequest`    | -  |
| 删除   | `DeleteLabelRequest`    | -  |

### 用户登陆限制管理

| 请求类型 | 请求名称                           | 备注 |
|------|--------------------------------|----|
| 列表查询 | `DescribeUserLoginACLsRequest` | -  |
| 详情查询 | `DetailUserLoginACLRequest`    | -  |
| 创建   | `CreateUserLoginACLRequest`    | -  |
| 更新   | `UpdateUserLoginACLRequest`    | -  |
| 删除   | `DeleteUserLoginACLRequest`    | -  |

### 登陆方法限制管理

| 请求类型 | 请求名称                               | 备注 |
|------|------------------------------------|----|
| 列表查询 | `DescribeConnectMethodACLsRequest` | -  |
| 详情查询 | `DetailConnectMethodACLRequest`    | -  |
| 创建   | `CreateConnectMethodACLRequest`    | -  |
| 更新   | `UpdateConnectMethodACLRequest`    | -  |
| 删除   | `DeleteConnectMethodACLRequest`    | -  |

### 命令过滤管理

| 请求类型     | 请求名称                            | 备注 |
|----------|---------------------------------|----|
| 命令过滤列表查询 | `DescribeCommandFiltersRequest` | -  |
| 命令过滤详情查询 | `DetailCommandFilterRequest`    | -  |
| 命令过滤创建   | `CreateCommandFilterRequest`    | -  |
| 命令过滤更新   | `UpdateCommandFilterRequest`    | -  |
| 命令过滤删除   | `DeleteCommandFilterRequest`    | -  |
| 命令组列表查询  | `DescribeCommandGroupsRequest`  | -  |
| 命令组详情查询  | `DetailCommandGroupRequest`     | -  |
| 命令组创建    | `CreateCommandGroupRequest`     | -  |
| 命令组更新    | `UpdateCommandGroupRequest`     | -  |
| 命令组删除    | `DeleteCommandGroupRequest`     | -  |

### 其他常用页面功能接口查询

| 请求类型            | 请求名称                                                                    | 备注 |
|-----------------|-------------------------------------------------------------------------|----|
| 查询`用户`对应的资产授权   | `DescribePermissionsRequest(user_id='user_id')`                         | -  |
| 查询`用户`对应的用户登陆规则 | `DescribeUserLoginACLsRequest(user='user_id')`                          | -  |
| 查询`用户`连接的资产会话   | `DescribeSessionsRequest(user_id='user_id')`                            | -  |
| 查询`用户组`下的用户列表   | `DescribeUsersRequest(group_id='group_id')`                             | -  |
| 查询`资产`下的账号列表    | `DescribeAccountsRequest(asset='asset_id')`                             | -  |
| 查询`资产`下的会话记录    | `DescribeSessionsRequest(asset_id='asset_id')`                          | -  |
| 查询`资产`下的命令记录    | `DescribeCommandsRequest(asset_id='asset_id')`                          | -  |
| 查询`网域`下的资产      | `DescribeAssetsRequest(domain='domain_id', exclude_platform='Gateway')` | -  |

## 安装与使用

### 安装(未实现，1.0 版本发布时同步上线)

```bash
pip install jumpserver-sdk
```
