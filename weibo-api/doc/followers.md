## followers

获取用户粉丝列表：

<https://open.weibo.com/wiki/2/friendships/followers>

API：

<https://api.weibo.com/2/friendships/followers.json>

|              | 必选  |  类型  |                             说明                             |
| :----------: | :---: | :----: | :----------------------------------------------------------: |
| access_token | true  | string |        采用OAuth授权方式为必填参数，OAuth授权后获得。        |
|     uid      | false | int64  |                     需要查询的用户UID。                      |
| screen_name  | false | string |                     需要查询的用户昵称。                     |
|    count     | false |  int   |          单页返回的记录条数，默认为5，最大不超过5。          |
|    cursor    | false |  int   | 返回结果的游标，下一页用返回值里的next_cursor，上一页用previous_cursor，默认为0。 |
| trim_status  | false |  int   | 返回值中user字段中的status字段开关，0：返回完整status字段、1：status字段仅返回status_id，默认为1。 |

> - 参数uid与screen_name二者必选其一，且只能选其一；
> - 接口升级后：uid与screen_name只能为当前授权用户；

## followers/ids

获取用户粉丝的用户UID列表：

<https://open.weibo.com/wiki/2/friendships/followers/ids>

API：

<https://api.weibo.com/2/friendships/followers/ids.json>

```
uid = 0
```