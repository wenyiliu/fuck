CREATE TABLE `yb_point_log_data` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '自增ID',
  `is_deleted` tinyint(3) unsigned NOT NULL DEFAULT 0 COMMENT '是否删除（0:未删除 1:已删除）',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '记录创建时间',
  `modify_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '记录修改时间',
  `creator` int(11) unsigned NOT NULL DEFAULT 0 COMMENT '创建人,0表示无创建人值',
  `modifier` int(11) unsigned NOT NULL DEFAULT 0 COMMENT '修改人,如果为0则表示纪录未修改',
  `user_id` int(11) unsigned NOT NULL DEFAULT 0 COMMENT '用户ID',
  `patient_id` int(11) unsigned NOT NULL DEFAULT 0 COMMENT '患者ID',
  `method_name` varchar(128) NOT NULL DEFAULT '' COMMENT '方法名',
  `path` varchar(256)  NOT NULL DEFAULT '0' COMMENT '路由',
  `referer` varchar(1000) NOT NULL DEFAULT '' COMMENT '来源页面',
  `timestamp` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '请求时间',
  `ip` varchar(30) NOT NULL DEFAULT  '' COMMENT '用户IP',
  `params` text  COMMENT '请求参数,json格式存储',
   PRIMARY KEY (`id`),
   KEY `idx_patient_id` (`patient_id`),
   KEY `idx_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='埋点数据';