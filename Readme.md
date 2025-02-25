# 项目描述

## 项目概述
本项目是针对 **JumpServer v3 最新版本** 开发的 **SDK（软件开发工具包）**。JumpServer 是一款开源的堡垒机系统，提供安全、高效的运维审计能力。本 SDK 旨在为开发者提供便捷的接口和工具，以便快速集成 JumpServer v3 的功能，实现自动化运维、资源管理、用户权限控制等操作。

---

## 项目目标
1. **简化集成**：提供简单易用的 API 接口，帮助开发者快速集成 JumpServer v3 的核心功能。
2. **功能覆盖**：支持 JumpServer v3 的主要功能模块，包括用户管理、资产管理、权限控制、会话审计等。
3. **提高效率**：通过 SDK 实现自动化操作，减少手动配置和管理的时间成本。
4. **兼容性与扩展性**：确保 SDK 兼容 JumpServer v3 的最新版本，并提供良好的扩展性，方便后续功能迭代。

---

## SDK 功能特性
目前 SDK 提供下方接口功能封装，使用详情请查看本项目 tests 目录下的测试用例

### **认证**
   - 基于 AccessKey 认证
   - 基于 账号/密码 认证

### **用户管理**
   - 列表查询 `DescribeUsersRequest`
   - 详情查询 `DetailUserRequest`
   - 创建 `CreateUserRequest`
   - 更新 `UpdateUserRequest`
   - 删除 `DeleteUserRequest`
   - 邀请 `InviteUserRequest`
   - 移除 `RemoveUserRequest`

### **用户组管理**
   - 列表查询
   - 详情查询
   - 创建
   - 更新
   - 删除

### **资产管理**
   - 列表查询 `DescribeAssetsRequest`
     - [可按照分类查询，Asset 可更换为 Host/Database/Cloud/Device/Web/GPT/Custom]
   - 详情查询 `DetailAssetRequest`
     - [可按照分类查询，同上]
   - 创建 `CreateHostRequest`
     - [`只`可按照具体分类查询，Host 可更换为 Database/Cloud/Device/Web/GPT/Custom]
   - 更新 `UpdateHostRequest`
     - [`只`可按照具体分类查询，同上]
   - 删除 `DeleteAssetRequest`
   - 批量删除 `BulkDeleteAssetRequest`

### **平台管理**
   - 列表查询 `DescribePlatformsRequest`
   - 详情查询 `DetailPlatformRequest`
   - 创建 `CreatePlatformRequest`
   - 更新 `UpdatePlatformRequest`
   - 删除 `DeletePlatformRequest`

### **网域管理**
   - 列表查询 `DescribeDomainsRequest`
   - 详情查询 `DetailDomainRequest`
   - 创建 `CreateDomainRequest`
   - 更新 `UpdateDomainRequest`
   - 删除 `DeleteDomainRequest`

### **节点管理**
   - 列表查询 `DescribeNodesRequest`
   - 详情查询 `DetailNodeRequest`
   - 创建 `CreateNodeRequest`
   - 更新 `CreateNodeRequest`
   - 删除 `DeleteNodeRequest`

### **组织管理**
   - 列表查询
   - 详情查询
   - 创建
   - 更新
   - 删除

### **权限管理**
   - 列表查询
   - 详情查询
   - 创建
   - 更新
   - 删除

### **审计管理**
   - 在线用户查询
   - 登录日志
   - 操作日志
   - 用户改密日志
   - 作业日志
   - FTP记录
   - 会话记录
   - 命令记录

### **标签管理**
   - 列表查询
   - 详情查询
   - 创建
   - 更新
   - 删除

### **用户登陆限制管理**
   - 列表查询
   - 详情查询
   - 创建
   - 更新
   - 删除

### **登陆方法限制管理**
   - 列表查询
   - 详情查询
   - 创建
   - 更新
   - 删除

### **命令过滤管理**
   - 命令过滤列表查询
   - 命令过滤详情查询
   - 命令过滤创建
   - 命令过滤更新
   - 命令过滤删除
   - 命令组列表查询
   - 命令组详情查询
   - 命令组创建
   - 命令组更新
   - 命令组删除

### **其他常用页面功能接口查询**
   - 根据`用户`查询对应的资产授权规则 `DescribePermissionsRequest(user_id='user_id')`
   - 根据`用户`查询对应的用户登陆规则 `DescribeUserLoginACLsRequest(user='user_id')`
   - 根据`用户`查询对应的用户会话 `DescribeSessionsRequest(user_id='user_id')`
   - 根据`用户组`查询对应的用户 `DescribeUsersRequest(group_id='group_id')`

## 安装与使用

### 安装(未实现，1.0 版本发布时同步上线)
```bash
pip install jumpserver-sdk
