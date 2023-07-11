<https://space.bilibili.com/34579852/dynamic>

## API URL

https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/space?host_mid=34579852

## URL参数

| 参数名             | 类型  | 必填  | 内容     | 备注                                                        |
|-----------------|-----|-----|--------|-----------------------------------------------------------|
| timezone_offset | str |     | `-480` |                                                           |
| type            | str |     | 分类     | `all`：全部<br/>`video`：视频投稿<br/>`pgc`：追番追剧<br/>`article`：专栏 |
| offset          | num |     | 分页偏移量  | 翻页时使用                                                     |
| update_baseline | str |     | 更新基线   | 获取新动态时使用                                                  |
| page            | num |     | 页数     | 无效参数                                                      |

## `data`对象

| 字段名             | 类型    | 内容             | 备注                               |
|-----------------|-------|----------------|----------------------------------|
| has_more        | bool  | 是否有更多数据        |                                  |
| items           | array | 数据数组           |                                  |
| offset          | str   | 偏移量            | 等于`items`中最后一条记录的id<br/>获取下一页时使用 |
| update_baseline | str   | 更新基线           | 等于`items`中第一条记录的id               |
| update_num      | num   | 本次获取获取到了多少条新动态 | 在更新基线以上的动态条数                     |

## `data`对象 -> `items`数组中的对象 -> `modules`对象 -> `module_dynamic`对象 -> `major`对象 -> `draw`对象 -> `items`数组中的对象

| 字段名    | 类型    | 内容    | 备注   |
|--------|-------|-------|------|
| height | num   | 图片高度  |      |
| size   | num   | 图片大小  | 单位KB |
| src    | str   | 图片URL |      |
| tags   | array |       |      |
| width  | num   | 图片宽度  |      |

## Reference

- <https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/dynamic/space.md>
- <https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/dynamic/all.md>
- 