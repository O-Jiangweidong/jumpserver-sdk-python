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

### **用户组管理**
   - 列表查询
   - 详情查询
   - 创建
   - 更新
   - 删除

### **资产管理**
   - 列表查询
   - 详情查询
   - 创建
   - 更新
   - 删除

### **平台管理**
   - 列表查询
   - 详情查询
   - 创建
   - 更新
   - 删除

### **网域管理**
   - 列表查询
   - 详情查询
   - 创建
   - 更新
   - 删除

### **节点管理**
   - 列表查询
   - 详情查询
   - 创建
   - 更新
   - 删除

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


## 安装与使用

### 安装
```bash
pip install jumpserver-sdk
