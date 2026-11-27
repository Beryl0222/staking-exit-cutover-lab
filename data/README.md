# 数据说明

所有数据均为合成资料。每张表的首行为字段名。

操作记录先按纪元和 sequence 排序，同纪元中链上事实先于操作，支付回报跟在操作之后。move 和 exit 以 source 标识的原批次内的未转移未退出份额为基准。初始各份额的风险记自 from_epoch。退出不改变 past risk，启动解绑之纪元是该部分风险仍覆盖的最后纪元。奖励和罚没金额按该纪元可归属的份额分摊，尾差保留在同验证者的池内，资产以十进制计算。入池的份额按当前该验证者仍活跃的资产净值计量，首笔 1:1。解锁必须达到 begin 加等待时长、相应风险纪元已过裁定最短等待且有明确 clear_through，并且记录 arrived 已收到。银行 submit 是待确认实际发款，仅满足条件的部分可认领，其金额也不能超过实际到账的待兑余额。

## slices

- `slice` 委托批次
- `owner` 基金份额持有人
- `validator` 验证者
- `from_epoch` 首个风险纪元
- `shares` 份额数
- `assets` 原始资产单位

## operations

- `op` 资金或份额操作号
- `epoch` 受理纪元
- `sequence` 纪元内时序
- `kind` deposit、move、exit、withdraw 或 begin
- `owner` 持有人
- `from` 来源批次、验证者或退出申请
- `to` 目标验证者，可空
- `amount` 资产或份额数量
- `ref` 对应申请

## validator_policy

- `validator` 验证者
- `unbind_epochs` 解绑等待纪元
- `safety_epochs` 超出风险纪元后最少的罚没裁定等待
- `scale` 资产和金额小数位

## chain_statements

- `event` 网关事实号
- `known_epoch` 可见纪元
- `kind` reward、slash、clear_through 或 arrived
- `validator` 验证者
- `risk_epoch` 覆盖纪元或确认裁定截至纪元
- `amount` 资产数量，clear_through 留空
- `ref` 解绑号，只有 arrived 有

## payment_updates

- `id` 收付回报身份
- `epoch` 到达纪元
- `kind` submit 或 paid
- `instruction` 银行付款身份
- `request` 退出申请
- `units` 资产数量
