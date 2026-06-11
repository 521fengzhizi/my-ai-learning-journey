# 云存储方案对比与选择

## 方案概览

| 特性 | JSONBin | Supabase | Firebase | GitHub Pages |
|------|---------|----------|----------|--------------|
| **免费配额** | 100 Bins | 500MB | 1GB | 无限 |
| **实时更新** | ❌ | ✅ | ✅ | ❌ |
| **数据库** | ❌ | ✅ | ✅ | ❌ |
| **认证支持** | ❌ | ✅ | ✅ | ✅ |
| **易用性** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **学习成本** | 很低 | 中等 | 中等 | 中等 |
| **适合场景** | 原型/演示 | 小中型项目 | 中大型项目 | 静态配置 |

---

## 1. JSONBin（推荐入门）

### 优点
- ✅ 极度简单易用
- ✅ 无需认证配置
- ✅ 开箱即用
- ✅ 免费配额足够

### 缺点
- ❌ 没有实时数据库
- ❌ 不支持复杂查询
- ❌ 免费版本有限制

### 价格
- **免费**: 100 Bins，100 请求/月（非常慷慨的免费版）
- **付费**: $4.99/月起

### 快速开始

```python
from cloud_sync import CloudSyncClient

client = CloudSyncClient(
    provider="jsonbin",
    jsonbin_id="5f8a7c1234567890abcdef",  # 从 JSONBin 获取
    api_key="$2b$10$..."  # 你的 Master Key
)

# 使用
client.set("data:key", {"value": 123})
data = client.get("data:key")
```

### 获取凭证

1. 访问 [JSONBin.io](https://jsonbin.io)
2. 注册账户
3. 创建新 Bin
4. 复制 Bin ID 和 Master Key

---

## 2. Supabase（推荐中型项目）

### 优点
- ✅ 完整数据库功能
- ✅ 实时数据库
- ✅ 内置认证系统
- ✅ 无需后端开发
- ✅ PostgreSQL 支持

### 缺点
- ⚠️ 需要一些配置
- ⚠️ 学习曲线较陡
- ⚠️ 免费版本有限制

### 价格
- **免费**: 500MB 数据库，50MB 文件存储
- **付费**: $25/月起

### 快速开始

```python
from cloud_sync import CloudSyncClient

client = CloudSyncClient(
    provider="supabase",
    url="https://your-project.supabase.co",
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    table="sync_data"
)

# 使用相同的 API
client.set("user:123:settings", {"theme": "dark"})
value = client.get("user:123:settings")
```

### 获取凭证

1. 访问 [Supabase](https://supabase.io)
2. 创建新项目
3. 进入 Settings > API
4. 复制 Project URL 和 Anon Key

### 数据库设置

```sql
-- 创建 sync_data 表
CREATE TABLE sync_data (
  id BIGSERIAL PRIMARY KEY,
  key TEXT UNIQUE NOT NULL,
  value JSONB NOT NULL,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- 启用实时更新
ALTER TABLE sync_data ENABLE ROW LEVEL SECURITY;

-- 创建公开策略
CREATE POLICY "Public access" ON sync_data
  FOR ALL USING (true) WITH CHECK (true);
```

---

## 3. Firebase Realtime Database

### 优点
- ✅ 谷歌完整生态
- ✅ 强大的实时数据库
- ✅ 完善的文档和社区
- ✅ 生产就绪

### 缺点
- ⚠️ 配置复杂
- ⚠️ 学习成本高
- ⚠️ 成本可能更高
- ⚠️ 对初学者不友好

### 价格
- **免费**: 1GB 存储，100 并发连接
- **付费**: 按量计费

### 快速开始

```python
from cloud_sync import CloudSyncClient

client = CloudSyncClient(
    provider="firebase",
    credentials_path="./firebase-key.json",
    database_url="https://your-project.firebaseio.com"
)

# 使用相同的 API
client.set("app/config", {"version": "1.0.0"})
```

### 获取凭证

1. 访问 [Firebase Console](https://console.firebase.google.com)
2. 创建项目
3. 启用 Realtime Database
4. 下载服务账户密钥 (JSON)

---

## 4. GitHub Pages + Actions（适合静态配置）

### 优点
- ✅ 完全免费
- ✅ 版本控制
- ✅ 与 GitHub 集成
- ✅ 无需额外账户

### 缺点
- ❌ 不是实时数据库
- ❌ 手动更新配置
- ❌ 不适合高频更新

### 使用场景

```
最适合存储：
- 应用版本信息
- 功能开关（Feature Flags）
- 静态配置文件
- 公开数据

不适合：
- 实时数据同步
- 用户个人数据
- 高频更新场景
```

### 快速开始

```yaml
# .github/workflows/deploy.yml
name: Deploy to Pages

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./config
```

---

## 选择指南

### 我应该选择哪个方案？

#### 🟢 选择 JSONBin，如果：
- 刚开始学习
- 做原型或演示
- 数据量小（< 10KB）
- 不需要复杂查询
- 需要最快的开始

```python
# JSONBin 示例
from cloud_sync import CloudSyncClient

client = CloudSyncClient(
    provider="jsonbin",
    jsonbin_id="YOUR_BIN_ID",
    api_key="YOUR_API_KEY"
)
```

#### 🟡 选择 Supabase，如果：
- 构建小到中型项目
- 需要实时数据库
- 想要内置认证
- 预算有限
- 想用 SQL

```python
# Supabase 示例
client = CloudSyncClient(
    provider="supabase",
    url="https://your-project.supabase.co",
    api_key="YOUR_ANON_KEY"
)
```

#### 🔴 选择 Firebase，如果：
- 构建中大型项目
- 需要完整的后端
- 有充足的预算
- 需要企业级支持
- 已经在使用 Google 生态

```python
# Firebase 示例
client = CloudSyncClient(
    provider="firebase",
    credentials_path="./firebase-key.json",
    database_url="https://your-project.firebaseio.com"
)
```

#### ⚪ 选择 GitHub Pages，如果：
- 只存储静态配置
- 数据很少更新
- 想要完全免费方案
- 重视版本控制

---

## 迁移指南

### JSONBin → Supabase

```python
# 导出数据
client_jsonbin = CloudSyncClient(provider="jsonbin", ...)
data = client_jsonbin.get("all_data")

# 导入到 Supabase
client_supabase = CloudSyncClient(provider="supabase", ...)
for key, value in data.items():
    client_supabase.set(key, value)
```

### 成本估算

#### 每月流量 10,000 请求

| 方案 | 成本 | 备注 |
|------|------|------|
| JSONBin | 免费 | 超过后 $4.99/月 |
| Supabase | 免费 | 包含在免费配额 |
| Firebase | ~$2 | 按量计费 |
| GitHub | 免费 | 无成本 |

---

## 安全考虑

### 敏感数据处理

```python
# ✅ 推荐：使用环境变量
import os

api_key = os.getenv("JSONBIN_API_KEY")

client = CloudSyncClient(
    provider="jsonbin",
    jsonbin_id=os.getenv("JSONBIN_ID"),
    api_key=api_key
)
```

```python
# ❌ 不推荐：直接在代码中
client = CloudSyncClient(
    provider="jsonbin",
    jsonbin_id="123456",
    api_key="actual_secret_key"  # 危险！
)
```

### 数据加密

```python
# 使用 HTTPS（所有方案都支持）
# JSONBin、Supabase、Firebase 都使用加密传输

# 可选：应用层加密
import json
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

# 加密
sensitive_data = {"password": "secret"}
encrypted = cipher.encrypt(json.dumps(sensitive_data).encode())
client.set("user:sensitive", encrypted.decode())

# 解密
encrypted_data = client.get("user:sensitive")
decrypted = cipher.decrypt(encrypted_data.encode())
data = json.loads(decrypted)
```

---

## 总结

| 需求 | 推荐方案 | 原因 |
|------|---------|------|
| 快速原型 | JSONBin | 最简单 |
| 小项目 | Supabase | 功能全面 |
| 大项目 | Firebase | 生产就绪 |
| 配置管理 | GitHub | 版本控制 |
| 学习 | JSONBin | 门槛低 |

