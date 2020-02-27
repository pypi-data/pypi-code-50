# fc_rules_cf_fc.py

from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def fc_default(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    build_cube_metadata(engine)
    engine.rule_triggered.add(rule.name)
    rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_provides_grid_mapping_rotated_latitude_longitude(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'grid_mapping', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_grid_mapping(engine, context.lookup_data('grid_mapping'), CF_GRID_MAPPING_ROTATED_LAT_LON):
          cf_grid_var = engine.cf_var.cf_group.grid_mappings[context.lookup_data('grid_mapping')]
          coordinate_system = build_rotated_coordinate_system(engine, cf_grid_var)
          engine.provides['coordinate_system'] = coordinate_system
          engine.assert_('facts_cf', 'provides',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_provides_grid_mapping_latitude_longitude(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'grid_mapping', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_grid_mapping(engine, context.lookup_data('grid_mapping'), CF_GRID_MAPPING_LAT_LON):
          cf_grid_var = engine.cf_var.cf_group.grid_mappings[context.lookup_data('grid_mapping')]
          coordinate_system = build_coordinate_system(cf_grid_var)
          engine.provides['coordinate_system'] = coordinate_system
          engine.assert_('facts_cf', 'provides',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_provides_grid_mapping_transverse_mercator(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'grid_mapping', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_grid_mapping(engine, context.lookup_data('grid_mapping'), CF_GRID_MAPPING_TRANSVERSE):
          cf_grid_var = engine.cf_var.cf_group.grid_mappings[context.lookup_data('grid_mapping')]
          coordinate_system = build_transverse_mercator_coordinate_system(engine, cf_grid_var)
          engine.provides['coordinate_system'] = coordinate_system
          engine.assert_('facts_cf', 'provides',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_provides_grid_mapping_mercator(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'grid_mapping', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_grid_mapping(engine, context.lookup_data('grid_mapping'), CF_GRID_MAPPING_MERCATOR):
          if has_supported_mercator_parameters(engine, context.lookup_data('grid_mapping')):
            cf_grid_var = engine.cf_var.cf_group.grid_mappings[context.lookup_data('grid_mapping')]
            coordinate_system = build_mercator_coordinate_system(engine, cf_grid_var)
            engine.provides['coordinate_system'] = coordinate_system
            engine.assert_('facts_cf', 'provides',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),)),
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_provides_grid_mapping_stereographic(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'grid_mapping', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_grid_mapping(engine, context.lookup_data('grid_mapping'), CF_GRID_MAPPING_STEREO):
          if has_supported_stereographic_parameters(engine, context.lookup_data('grid_mapping')):
            cf_grid_var = engine.cf_var.cf_group.grid_mappings[context.lookup_data('grid_mapping')]
            coordinate_system = build_stereographic_coordinate_system(engine, cf_grid_var)
            engine.provides['coordinate_system'] = coordinate_system
            engine.assert_('facts_cf', 'provides',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),)),
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_provides_grid_mapping_lambert_conformal(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'grid_mapping', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_grid_mapping(engine, context.lookup_data('grid_mapping'), CF_GRID_MAPPING_LAMBERT_CONFORMAL):
          cf_grid_var = engine.cf_var.cf_group.grid_mappings[context.lookup_data('grid_mapping')]
          coordinate_system = build_lambert_conformal_coordinate_system(engine, cf_grid_var)
          engine.provides['coordinate_system'] = coordinate_system
          engine.assert_('facts_cf', 'provides',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_provides_grid_mapping_lambert_azimuthal_equal_area(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'grid_mapping', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_grid_mapping(engine, context.lookup_data('grid_mapping'), CF_GRID_MAPPING_LAMBERT_AZIMUTHAL):
          cf_grid_var = engine.cf_var.cf_group.grid_mappings[context.lookup_data('grid_mapping')]
          coordinate_system = build_lambert_azimuthal_equal_area_coordinate_system(engine, cf_grid_var)
          engine.provides['coordinate_system'] = coordinate_system
          engine.assert_('facts_cf', 'provides',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_provides_grid_mapping_albers_equal_area(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'grid_mapping', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_grid_mapping(engine, context.lookup_data('grid_mapping'), CF_GRID_MAPPING_ALBERS):
          cf_grid_var = engine.cf_var.cf_group.grid_mappings[context.lookup_data('grid_mapping')]
          coordinate_system = build_albers_equal_area_coordinate_system(engine, cf_grid_var)
          engine.provides['coordinate_system'] = coordinate_system
          engine.assert_('facts_cf', 'provides',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_provides_grid_mapping_vertical_perspective(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'grid_mapping', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_grid_mapping(engine, context.lookup_data('grid_mapping'), CF_GRID_MAPPING_VERTICAL):
          cf_grid_var = engine.cf_var.cf_group.grid_mappings[context.lookup_data('grid_mapping')]
          coordinate_system = \
                      build_vertical_perspective_coordinate_system(engine, cf_grid_var)
          engine.provides['coordinate_system'] = coordinate_system
          engine.assert_('facts_cf', 'provides',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_provides_grid_mapping_geostationary(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'grid_mapping', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_grid_mapping(engine, context.lookup_data('grid_mapping'),
           CF_GRID_MAPPING_GEOSTATIONARY):
          cf_grid_var = engine.cf_var.cf_group.grid_mappings[context.lookup_data('grid_mapping')]
          coordinate_system = \
                      build_geostationary_coordinate_system(engine, cf_grid_var)
          engine.provides['coordinate_system'] = coordinate_system
          engine.assert_('facts_cf', 'provides',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_provides_coordinate_latitude(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'coordinate', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_latitude(engine, context.lookup_data('coordinate')):
          engine.assert_('facts_cf', 'provides',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_provides_coordinate_longitude(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'coordinate', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_longitude(engine, context.lookup_data('coordinate')):
          engine.assert_('facts_cf', 'provides',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_provides_projection_x_coordinate(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'coordinate', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_projection_x_coordinate(engine, context.lookup_data('coordinate')):
          engine.assert_('facts_cf', 'provides',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_provides_projection_y_coordinate(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'coordinate', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_projection_y_coordinate(engine, context.lookup_data('coordinate')):
          engine.assert_('facts_cf', 'provides',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_provides_coordinate_time(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'coordinate', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_time(engine, context.lookup_data('coordinate')):
          engine.assert_('facts_cf', 'provides',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_provides_coordinate_time_period(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'coordinate', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_time_period(engine, context.lookup_data('coordinate')):
          engine.assert_('facts_cf', 'provides',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_label_coordinate(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'label', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        cf_coord_var = engine.cf_var.cf_group.labels[context.lookup_data('coordinate')]
        build_auxiliary_coordinate(engine, cf_coord_var)
        engine.rule_triggered.add(rule.name)
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_auxiliary_coordinate_time(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'auxiliary_coordinate', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_time(engine, context.lookup_data('coordinate')):
          cf_coord_var = engine.cf_var.cf_group.auxiliary_coordinates[context.lookup_data('coordinate')]
          build_auxiliary_coordinate(engine, cf_coord_var)
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_auxiliary_coordinate_time_period(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'auxiliary_coordinate', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_time_period(engine, context.lookup_data('coordinate')):
          cf_coord_var = engine.cf_var.cf_group.auxiliary_coordinates[context.lookup_data('coordinate')]
          build_auxiliary_coordinate(engine, cf_coord_var)
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_auxiliary_coordinate_latitude(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'auxiliary_coordinate', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_latitude(engine, context.lookup_data('coordinate')):
          if not is_rotated_latitude(engine, context.lookup_data('coordinate')):
            cf_coord_var = engine.cf_var.cf_group.auxiliary_coordinates[context.lookup_data('coordinate')]
            build_auxiliary_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_LAT)
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_auxiliary_coordinate_latitude_rotated(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'auxiliary_coordinate', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_latitude(engine, context.lookup_data('coordinate')):
          if is_rotated_latitude(engine, context.lookup_data('coordinate')):
            cf_coord_var = engine.cf_var.cf_group.auxiliary_coordinates[context.lookup_data('coordinate')]
            build_auxiliary_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_GRID_LAT)
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_auxiliary_coordinate_longitude(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'auxiliary_coordinate', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_longitude(engine, context.lookup_data('coordinate')):
          if not is_rotated_longitude(engine, context.lookup_data('coordinate')):
            cf_coord_var = engine.cf_var.cf_group.auxiliary_coordinates[context.lookup_data('coordinate')]
            build_auxiliary_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_LON)
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_auxiliary_coordinate_longitude_rotated(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'auxiliary_coordinate', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if is_longitude(engine, context.lookup_data('coordinate')):
          if is_rotated_longitude(engine, context.lookup_data('coordinate')):
            cf_coord_var = engine.cf_var.cf_group.auxiliary_coordinates[context.lookup_data('coordinate')]
            build_auxiliary_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_GRID_LON)
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_auxiliary_coordinate(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'auxiliary_coordinate', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if not is_time(engine, context.lookup_data('coordinate')):
          if not is_time_period(engine, context.lookup_data('coordinate')):
            if not is_latitude(engine, context.lookup_data('coordinate')):
              if not is_longitude(engine, context.lookup_data('coordinate')):
                cf_coord_var = engine.cf_var.cf_group.auxiliary_coordinates[context.lookup_data('coordinate')]
                build_auxiliary_coordinate(engine, cf_coord_var)
                engine.rule_triggered.add(rule.name)
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_cell_measure(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'cell_measure', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        cf_coord_var = engine.cf_var.cf_group.cell_measures[context.lookup_data('coordinate')]
        build_cell_measures(engine, cf_coord_var)
        engine.rule_triggered.add(rule.name)
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_latitude(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if not is_rotated_latitude(engine, context.lookup_data('coordinate')):
              cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
              build_dimension_coordinate(engine, cf_coord_var,
              coord_name=CF_VALUE_STD_NAME_LAT,
              coord_system=engine.provides['coordinate_system'])
              engine.rule_triggered.add(rule.name)
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_latitude_rotated(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if is_rotated_latitude(engine, context.lookup_data('coordinate')):
              cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
              build_dimension_coordinate(engine, cf_coord_var,
              coord_name=CF_VALUE_STD_NAME_GRID_LAT,
              coord_system=engine.provides['coordinate_system'])
              engine.rule_triggered.add(rule.name)
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_longitude(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if not is_rotated_longitude(engine, context.lookup_data('coordinate')):
              cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
              build_dimension_coordinate(engine, cf_coord_var,
              coord_name=CF_VALUE_STD_NAME_LON,
              coord_system=engine.provides['coordinate_system'])
              engine.rule_triggered.add(rule.name)
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_longitude_rotated(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if is_rotated_longitude(engine, context.lookup_data('coordinate')):
              cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
              build_dimension_coordinate(engine, cf_coord_var,
              coord_name=CF_VALUE_STD_NAME_GRID_LON,
              coord_system=engine.provides['coordinate_system'])
              engine.rule_triggered.add(rule.name)
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_latitude_nocs(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        notany596_worked = True
        with engine.lookup('facts_cf', 'provides', context, \
                           rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            notany596_worked = False
            if not notany596_worked: break
        if notany596_worked:
          notany598_worked = True
          with engine.lookup('facts_cf', 'provides', context, \
                             rule.foreach_patterns(2)) \
            as gen_2:
            for dummy in gen_2:
              notany598_worked = False
              if not notany598_worked: break
          if notany598_worked:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_LAT,
            coord_system=None)
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_longitude_nocs(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        notany619_worked = True
        with engine.lookup('facts_cf', 'provides', context, \
                           rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            notany619_worked = False
            if not notany619_worked: break
        if notany619_worked:
          notany621_worked = True
          with engine.lookup('facts_cf', 'provides', context, \
                             rule.foreach_patterns(2)) \
            as gen_2:
            for dummy in gen_2:
              notany621_worked = False
              if not notany621_worked: break
          if notany621_worked:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_LON,
            coord_system=None)
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_projection_x_transverse_mercator(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_PROJ_X,
            coord_system=engine.provides['coordinate_system'])
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_projection_y_transverse_mercator(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_PROJ_Y,
            coord_system=engine.provides['coordinate_system'])
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_projection_x_lambert_conformal(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_PROJ_X,
            coord_system=engine.provides['coordinate_system'])
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_projection_y_lambert_conformal(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_PROJ_Y,
            coord_system=engine.provides['coordinate_system'])
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_projection_x_mercator(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_PROJ_X,
            coord_system=engine.provides['coordinate_system'])
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_projection_y_mercator(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_PROJ_Y,
            coord_system=engine.provides['coordinate_system'])
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_projection_x_stereographic(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_PROJ_X,
            coord_system=engine.provides['coordinate_system'])
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_projection_y_stereographic(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_PROJ_Y,
            coord_system=engine.provides['coordinate_system'])
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_projection_x_lambert_azimuthal_equal_area(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_PROJ_X,
            coord_system=engine.provides['coordinate_system'])
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_projection_y_lambert_azimuthal_equal_area(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_PROJ_Y,
            coord_system=engine.provides['coordinate_system'])
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_projection_x_albers_equal_area(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_PROJ_X,
            coord_system=engine.provides['coordinate_system'])
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_projection_y_albers_equal_area(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_PROJ_Y,
            coord_system=engine.provides['coordinate_system'])
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_projection_x_vertical_perspective(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_PROJ_X,
            coord_system=engine.provides['coordinate_system'])
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_projection_y_vertical_perspective(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_PROJ_Y,
            coord_system=engine.provides['coordinate_system'])
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_projection_x_geostationary(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_PROJ_X,
            coord_system=engine.provides['coordinate_system'])
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_projection_y_geostationary(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'provides', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
            build_dimension_coordinate(engine, cf_coord_var,
            coord_name=CF_VALUE_STD_NAME_PROJ_Y,
            coord_system=engine.provides['coordinate_system'])
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_time(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
        build_dimension_coordinate(engine, cf_coord_var)
        engine.rule_triggered.add(rule.name)
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_build_coordinate_time_period(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'provides', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
        build_dimension_coordinate(engine, cf_coord_var)
        engine.rule_triggered.add(rule.name)
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_default_coordinate(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'coordinate', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        notany987_worked = True
        with engine.lookup('facts_cf', 'provides', context, \
                           rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            notany987_worked = False
            if not notany987_worked: break
        if notany987_worked:
          cf_coord_var = engine.cf_var.cf_group.coordinates[context.lookup_data('coordinate')]
          build_dimension_coordinate(engine, cf_coord_var)
          engine.assert_('facts_cf', 'provides',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_attribute_ukmo__um_stash_source(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    if hasattr(engine.cf_var, 'ukmo__um_stash_source') or hasattr(engine.cf_var, 'um_stash_source'):
      attr_value = getattr(engine.cf_var, 'um_stash_source', None) or getattr(engine.cf_var, 'ukmo__um_stash_source')
      engine.cube.attributes['STASH'] = pp.STASH.from_msi(attr_value)
      engine.rule_triggered.add(rule.name)
      rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_attribute_ukmo__process_flags(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    if hasattr(engine.cf_var, 'ukmo__process_flags'):
      attr_value = engine.cf_var.ukmo__process_flags
      engine.cube.attributes['ukmo__process_flags'] = tuple([x.replace("_", " ") for x in attr_value.split(" ")])
      engine.rule_triggered.add(rule.name)
      rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_formula_type_atmosphere_hybrid_height_coordinate(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'formula_root', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if getattr(engine.cf_var.cf_group[context.lookup_data('coordinate')], 'standard_name') == 'atmosphere_hybrid_height_coordinate':
          engine.requires['formula_type'] = 'atmosphere_hybrid_height_coordinate'
          engine.assert_('facts_cf', 'formula_type',
                         (rule.pattern(0).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_formula_type_atmosphere_hybrid_sigma_pressure_coordinate(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'formula_root', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if getattr(engine.cf_var.cf_group[context.lookup_data('coordinate')], 'standard_name') == 'atmosphere_hybrid_sigma_pressure_coordinate':
          engine.requires['formula_type'] = 'atmosphere_hybrid_sigma_pressure_coordinate'
          engine.assert_('facts_cf', 'formula_type',
                         (rule.pattern(0).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_formula_type_ocean_sigma_z_coordinate(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'formula_root', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if getattr(engine.cf_var.cf_group[context.lookup_data('coordinate')], 'standard_name') == 'ocean_sigma_z_coordinate':
          engine.requires['formula_type'] = 'ocean_sigma_z_coordinate'
          engine.assert_('facts_cf', 'formula_type',
                         (rule.pattern(0).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_formula_type_ocean_sigma_coordinate(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'formula_root', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if getattr(engine.cf_var.cf_group[context.lookup_data('coordinate')], 'standard_name') == 'ocean_sigma_coordinate':
          engine.requires['formula_type'] = 'ocean_sigma_coordinate'
          engine.assert_('facts_cf', 'formula_type',
                         (rule.pattern(0).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_formula_type_ocean_s_coordinate(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'formula_root', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if getattr(engine.cf_var.cf_group[context.lookup_data('coordinate')], 'standard_name') == 'ocean_s_coordinate':
          engine.requires['formula_type'] = 'ocean_s_coordinate'
          engine.assert_('facts_cf', 'formula_type',
                         (rule.pattern(0).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_formula_type_ocean_s_coordinate_g1(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'formula_root', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if getattr(engine.cf_var.cf_group[context.lookup_data('coordinate')], 'standard_name') == 'ocean_s_coordinate_g1':
          engine.requires['formula_type'] = 'ocean_s_coordinate_g1'
          engine.assert_('facts_cf', 'formula_type',
                         (rule.pattern(0).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_formula_type_ocean_s_coordinate_g2(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'formula_root', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if getattr(engine.cf_var.cf_group[context.lookup_data('coordinate')], 'standard_name') == 'ocean_s_coordinate_g2':
          engine.requires['formula_type'] = 'ocean_s_coordinate_g2'
          engine.assert_('facts_cf', 'formula_type',
                         (rule.pattern(0).as_data(context),)),
          engine.rule_triggered.add(rule.name)
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def fc_formula_terms(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts_cf', 'formula_root', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('facts_cf', 'formula_term', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.requires.setdefault('formula_terms', {})[context.lookup_data('term')] = context.lookup_data('var_name')
            engine.rule_triggered.add(rule.name)
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('fc_rules_cf')
  
  fc_rule.fc_rule('fc_default', This_rule_base, fc_default,
    (),
    ())
  
  fc_rule.fc_rule('fc_provides_grid_mapping_rotated_latitude_longitude', This_rule_base, fc_provides_grid_mapping_rotated_latitude_longitude,
    (('facts_cf', 'grid_mapping',
      (contexts.variable('grid_mapping'),),
      False),),
    (pattern.pattern_literal('coordinate_system'),
     pattern.pattern_literal('rotated_latitude_longitude'),))
  
  fc_rule.fc_rule('fc_provides_grid_mapping_latitude_longitude', This_rule_base, fc_provides_grid_mapping_latitude_longitude,
    (('facts_cf', 'grid_mapping',
      (contexts.variable('grid_mapping'),),
      False),),
    (pattern.pattern_literal('coordinate_system'),
     pattern.pattern_literal('latitude_longitude'),))
  
  fc_rule.fc_rule('fc_provides_grid_mapping_transverse_mercator', This_rule_base, fc_provides_grid_mapping_transverse_mercator,
    (('facts_cf', 'grid_mapping',
      (contexts.variable('grid_mapping'),),
      False),),
    (pattern.pattern_literal('coordinate_system'),
     pattern.pattern_literal('transverse_mercator'),))
  
  fc_rule.fc_rule('fc_provides_grid_mapping_mercator', This_rule_base, fc_provides_grid_mapping_mercator,
    (('facts_cf', 'grid_mapping',
      (contexts.variable('grid_mapping'),),
      False),),
    (pattern.pattern_literal('coordinate_system'),
     pattern.pattern_literal('mercator'),))
  
  fc_rule.fc_rule('fc_provides_grid_mapping_stereographic', This_rule_base, fc_provides_grid_mapping_stereographic,
    (('facts_cf', 'grid_mapping',
      (contexts.variable('grid_mapping'),),
      False),),
    (pattern.pattern_literal('coordinate_system'),
     pattern.pattern_literal('stereographic'),))
  
  fc_rule.fc_rule('fc_provides_grid_mapping_lambert_conformal', This_rule_base, fc_provides_grid_mapping_lambert_conformal,
    (('facts_cf', 'grid_mapping',
      (contexts.variable('grid_mapping'),),
      False),),
    (pattern.pattern_literal('coordinate_system'),
     pattern.pattern_literal('lambert_conformal'),))
  
  fc_rule.fc_rule('fc_provides_grid_mapping_lambert_azimuthal_equal_area', This_rule_base, fc_provides_grid_mapping_lambert_azimuthal_equal_area,
    (('facts_cf', 'grid_mapping',
      (contexts.variable('grid_mapping'),),
      False),),
    (pattern.pattern_literal('coordinate_system'),
     pattern.pattern_literal('lambert_azimuthal_equal_area'),))
  
  fc_rule.fc_rule('fc_provides_grid_mapping_albers_equal_area', This_rule_base, fc_provides_grid_mapping_albers_equal_area,
    (('facts_cf', 'grid_mapping',
      (contexts.variable('grid_mapping'),),
      False),),
    (pattern.pattern_literal('coordinate_system'),
     pattern.pattern_literal('albers_equal_area'),))
  
  fc_rule.fc_rule('fc_provides_grid_mapping_vertical_perspective', This_rule_base, fc_provides_grid_mapping_vertical_perspective,
    (('facts_cf', 'grid_mapping',
      (contexts.variable('grid_mapping'),),
      False),),
    (pattern.pattern_literal('coordinate_system'),
     pattern.pattern_literal('vertical_perspective'),))
  
  fc_rule.fc_rule('fc_provides_grid_mapping_geostationary', This_rule_base, fc_provides_grid_mapping_geostationary,
    (('facts_cf', 'grid_mapping',
      (contexts.variable('grid_mapping'),),
      False),),
    (pattern.pattern_literal('coordinate_system'),
     pattern.pattern_literal('geostationary'),))
  
  fc_rule.fc_rule('fc_provides_coordinate_latitude', This_rule_base, fc_provides_coordinate_latitude,
    (('facts_cf', 'coordinate',
      (contexts.variable('coordinate'),),
      False),),
    (pattern.pattern_literal('coordinate'),
     pattern.pattern_literal('latitude'),
     contexts.variable('coordinate'),))
  
  fc_rule.fc_rule('fc_provides_coordinate_longitude', This_rule_base, fc_provides_coordinate_longitude,
    (('facts_cf', 'coordinate',
      (contexts.variable('coordinate'),),
      False),),
    (pattern.pattern_literal('coordinate'),
     pattern.pattern_literal('longitude'),
     contexts.variable('coordinate'),))
  
  fc_rule.fc_rule('fc_provides_projection_x_coordinate', This_rule_base, fc_provides_projection_x_coordinate,
    (('facts_cf', 'coordinate',
      (contexts.variable('coordinate'),),
      False),),
    (pattern.pattern_literal('coordinate'),
     pattern.pattern_literal('projection_x_coordinate'),
     contexts.variable('coordinate'),))
  
  fc_rule.fc_rule('fc_provides_projection_y_coordinate', This_rule_base, fc_provides_projection_y_coordinate,
    (('facts_cf', 'coordinate',
      (contexts.variable('coordinate'),),
      False),),
    (pattern.pattern_literal('coordinate'),
     pattern.pattern_literal('projection_y_coordinate'),
     contexts.variable('coordinate'),))
  
  fc_rule.fc_rule('fc_provides_coordinate_time', This_rule_base, fc_provides_coordinate_time,
    (('facts_cf', 'coordinate',
      (contexts.variable('coordinate'),),
      False),),
    (pattern.pattern_literal('coordinate'),
     pattern.pattern_literal('time'),
     contexts.variable('coordinate'),))
  
  fc_rule.fc_rule('fc_provides_coordinate_time_period', This_rule_base, fc_provides_coordinate_time_period,
    (('facts_cf', 'coordinate',
      (contexts.variable('coordinate'),),
      False),),
    (pattern.pattern_literal('coordinate'),
     pattern.pattern_literal('time_period'),
     contexts.variable('coordinate'),))
  
  fc_rule.fc_rule('fc_build_label_coordinate', This_rule_base, fc_build_label_coordinate,
    (('facts_cf', 'label',
      (contexts.variable('coordinate'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_auxiliary_coordinate_time', This_rule_base, fc_build_auxiliary_coordinate_time,
    (('facts_cf', 'auxiliary_coordinate',
      (contexts.variable('coordinate'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_auxiliary_coordinate_time_period', This_rule_base, fc_build_auxiliary_coordinate_time_period,
    (('facts_cf', 'auxiliary_coordinate',
      (contexts.variable('coordinate'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_auxiliary_coordinate_latitude', This_rule_base, fc_build_auxiliary_coordinate_latitude,
    (('facts_cf', 'auxiliary_coordinate',
      (contexts.variable('coordinate'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_auxiliary_coordinate_latitude_rotated', This_rule_base, fc_build_auxiliary_coordinate_latitude_rotated,
    (('facts_cf', 'auxiliary_coordinate',
      (contexts.variable('coordinate'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_auxiliary_coordinate_longitude', This_rule_base, fc_build_auxiliary_coordinate_longitude,
    (('facts_cf', 'auxiliary_coordinate',
      (contexts.variable('coordinate'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_auxiliary_coordinate_longitude_rotated', This_rule_base, fc_build_auxiliary_coordinate_longitude_rotated,
    (('facts_cf', 'auxiliary_coordinate',
      (contexts.variable('coordinate'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_auxiliary_coordinate', This_rule_base, fc_build_auxiliary_coordinate,
    (('facts_cf', 'auxiliary_coordinate',
      (contexts.variable('coordinate'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_cell_measure', This_rule_base, fc_build_cell_measure,
    (('facts_cf', 'cell_measure',
      (contexts.variable('coordinate'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_latitude', This_rule_base, fc_build_coordinate_latitude,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('latitude'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('latitude_longitude'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_latitude_rotated', This_rule_base, fc_build_coordinate_latitude_rotated,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('latitude'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('rotated_latitude_longitude'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_longitude', This_rule_base, fc_build_coordinate_longitude,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('longitude'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('latitude_longitude'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_longitude_rotated', This_rule_base, fc_build_coordinate_longitude_rotated,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('longitude'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('rotated_latitude_longitude'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_latitude_nocs', This_rule_base, fc_build_coordinate_latitude_nocs,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('latitude'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('latitude_longitude'),),
      True),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('rotated_latitude_longitude'),),
      True),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_longitude_nocs', This_rule_base, fc_build_coordinate_longitude_nocs,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('longitude'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('latitude_longitude'),),
      True),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('rotated_latitude_longitude'),),
      True),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_projection_x_transverse_mercator', This_rule_base, fc_build_coordinate_projection_x_transverse_mercator,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('projection_x_coordinate'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('transverse_mercator'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_projection_y_transverse_mercator', This_rule_base, fc_build_coordinate_projection_y_transverse_mercator,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('projection_y_coordinate'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('transverse_mercator'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_projection_x_lambert_conformal', This_rule_base, fc_build_coordinate_projection_x_lambert_conformal,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('projection_x_coordinate'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('lambert_conformal'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_projection_y_lambert_conformal', This_rule_base, fc_build_coordinate_projection_y_lambert_conformal,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('projection_y_coordinate'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('lambert_conformal'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_projection_x_mercator', This_rule_base, fc_build_coordinate_projection_x_mercator,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('projection_x_coordinate'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('mercator'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_projection_y_mercator', This_rule_base, fc_build_coordinate_projection_y_mercator,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('projection_y_coordinate'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('mercator'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_projection_x_stereographic', This_rule_base, fc_build_coordinate_projection_x_stereographic,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('projection_x_coordinate'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('stereographic'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_projection_y_stereographic', This_rule_base, fc_build_coordinate_projection_y_stereographic,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('projection_y_coordinate'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('stereographic'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_projection_x_lambert_azimuthal_equal_area', This_rule_base, fc_build_coordinate_projection_x_lambert_azimuthal_equal_area,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('projection_x_coordinate'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('lambert_azimuthal_equal_area'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_projection_y_lambert_azimuthal_equal_area', This_rule_base, fc_build_coordinate_projection_y_lambert_azimuthal_equal_area,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('projection_y_coordinate'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('lambert_azimuthal_equal_area'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_projection_x_albers_equal_area', This_rule_base, fc_build_coordinate_projection_x_albers_equal_area,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('projection_x_coordinate'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('albers_equal_area'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_projection_y_albers_equal_area', This_rule_base, fc_build_coordinate_projection_y_albers_equal_area,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('projection_y_coordinate'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('albers_equal_area'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_projection_x_vertical_perspective', This_rule_base, fc_build_coordinate_projection_x_vertical_perspective,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('projection_x_coordinate'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('vertical_perspective'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_projection_y_vertical_perspective', This_rule_base, fc_build_coordinate_projection_y_vertical_perspective,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('projection_y_coordinate'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('vertical_perspective'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_projection_x_geostationary', This_rule_base, fc_build_coordinate_projection_x_geostationary,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('projection_x_coordinate'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('geostationary'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_projection_y_geostationary', This_rule_base, fc_build_coordinate_projection_y_geostationary,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('projection_y_coordinate'),
       contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate_system'),
       pattern.pattern_literal('geostationary'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_time', This_rule_base, fc_build_coordinate_time,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('time'),
       contexts.variable('coordinate'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_build_coordinate_time_period', This_rule_base, fc_build_coordinate_time_period,
    (('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       pattern.pattern_literal('time_period'),
       contexts.variable('coordinate'),),
      False),),
    ())
  
  fc_rule.fc_rule('fc_default_coordinate', This_rule_base, fc_default_coordinate,
    (('facts_cf', 'coordinate',
      (contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'provides',
      (pattern.pattern_literal('coordinate'),
       contexts.anonymous('_'),
       contexts.variable('coordinate'),),
      True),),
    (pattern.pattern_literal('coordinate'),
     pattern.pattern_literal('miscellaneous'),
     contexts.variable('coordinate'),))
  
  fc_rule.fc_rule('fc_attribute_ukmo__um_stash_source', This_rule_base, fc_attribute_ukmo__um_stash_source,
    (),
    ())
  
  fc_rule.fc_rule('fc_attribute_ukmo__process_flags', This_rule_base, fc_attribute_ukmo__process_flags,
    (),
    ())
  
  fc_rule.fc_rule('fc_formula_type_atmosphere_hybrid_height_coordinate', This_rule_base, fc_formula_type_atmosphere_hybrid_height_coordinate,
    (('facts_cf', 'formula_root',
      (contexts.variable('coordinate'),),
      False),),
    (pattern.pattern_literal('atmosphere_hybrid_height_coordinate'),))
  
  fc_rule.fc_rule('fc_formula_type_atmosphere_hybrid_sigma_pressure_coordinate', This_rule_base, fc_formula_type_atmosphere_hybrid_sigma_pressure_coordinate,
    (('facts_cf', 'formula_root',
      (contexts.variable('coordinate'),),
      False),),
    (pattern.pattern_literal('atmosphere_hybrid_height_coordinate'),))
  
  fc_rule.fc_rule('fc_formula_type_ocean_sigma_z_coordinate', This_rule_base, fc_formula_type_ocean_sigma_z_coordinate,
    (('facts_cf', 'formula_root',
      (contexts.variable('coordinate'),),
      False),),
    (pattern.pattern_literal('ocean_sigma_z_coordinate'),))
  
  fc_rule.fc_rule('fc_formula_type_ocean_sigma_coordinate', This_rule_base, fc_formula_type_ocean_sigma_coordinate,
    (('facts_cf', 'formula_root',
      (contexts.variable('coordinate'),),
      False),),
    (pattern.pattern_literal('ocean_sigma_coordinate'),))
  
  fc_rule.fc_rule('fc_formula_type_ocean_s_coordinate', This_rule_base, fc_formula_type_ocean_s_coordinate,
    (('facts_cf', 'formula_root',
      (contexts.variable('coordinate'),),
      False),),
    (pattern.pattern_literal('ocean_s_coordinate'),))
  
  fc_rule.fc_rule('fc_formula_type_ocean_s_coordinate_g1', This_rule_base, fc_formula_type_ocean_s_coordinate_g1,
    (('facts_cf', 'formula_root',
      (contexts.variable('coordinate'),),
      False),),
    (pattern.pattern_literal('ocean_s_coordinate_g1'),))
  
  fc_rule.fc_rule('fc_formula_type_ocean_s_coordinate_g2', This_rule_base, fc_formula_type_ocean_s_coordinate_g2,
    (('facts_cf', 'formula_root',
      (contexts.variable('coordinate'),),
      False),),
    (pattern.pattern_literal('ocean_s_coordinate_g2'),))
  
  fc_rule.fc_rule('fc_formula_terms', This_rule_base, fc_formula_terms,
    (('facts_cf', 'formula_root',
      (contexts.variable('coordinate'),),
      False),
     ('facts_cf', 'formula_term',
      (contexts.variable('var_name'),
       contexts.variable('coordinate'),
       contexts.variable('term'),),
      False),),
    ())

import warnings
import cf_units
import netCDF4
import numpy as np
import numpy.ma as ma
import iris.aux_factory
from iris.common.mixin import _get_valid_standard_name
import iris.coords
import iris.coord_systems
import iris.fileformats.cf as cf
import iris.fileformats.netcdf
from iris.fileformats.netcdf import _get_cf_var_data, parse_cell_methods, UnknownCellMethodWarning
import iris.fileformats.pp as pp
import iris.exceptions
import iris.std_names
import iris.util
from iris._lazy_data import as_lazy_data
UD_UNITS_LAT = ['degrees_north', 'degree_north', 'degree_n', 'degrees_n',
                'degreen', 'degreesn', 'degrees', 'degrees north',
                'degree north', 'degree n', 'degrees n']
UD_UNITS_LON = ['degrees_east', 'degree_east', 'degree_e', 'degrees_e',
                'degreee', 'degreese', 'degrees', 'degrees east',
                'degree east', 'degree e', 'degrees e']
CF_COORD_VERTICAL = {'atmosphere_ln_pressure_coordinate':['p0', 'lev'],
                     'atmosphere_sigma_coordinate':['sigma', 'ps', 'ptop'],
                     'atmosphere_hybrid_sigma_pressure_coordinate':['a', 'b', 'ps', 'p0'],
                     'atmosphere_hybrid_height_coordinate':['a', 'b', 'orog'],
                     'atmosphere_sleve_coordinate':['a', 'b1', 'b2', 'ztop', 'zsurf1', 'zsurf2'],
                     'ocean_sigma_coordinate':['sigma', 'eta', 'depth'],
                     'ocean_s_coordinate':['s', 'eta', 'depth', 'a', 'b', 'depth_c'],
                     'ocean_sigma_z_coordinate':['sigma', 'eta', 'depth', 'depth_c', 'nsigma', 'zlev'],
                     'ocean_double_sigma_coordinate':['sigma', 'depth', 'z1', 'z2', 'a', 'href', 'k_c'],
                     'ocean_s_coordinate_g1':['s', 'eta', 'depth', 'depth_c', 'C'],
                     'ocean_s_coordinate_g2':['s', 'eta', 'depth', 'depth_c', 'C']}
CF_GRID_MAPPING_ALBERS = 'albers_conical_equal_area'
CF_GRID_MAPPING_AZIMUTHAL = 'azimuthal_equidistant'
CF_GRID_MAPPING_LAMBERT_AZIMUTHAL = 'lambert_azimuthal_equal_area'
CF_GRID_MAPPING_LAMBERT_CONFORMAL = 'lambert_conformal_conic'
CF_GRID_MAPPING_LAMBERT_CYLINDRICAL = 'lambert_cylindrical_equal_area'
CF_GRID_MAPPING_LAT_LON = 'latitude_longitude'
CF_GRID_MAPPING_MERCATOR = 'mercator'
CF_GRID_MAPPING_ORTHO = 'orthographic'
CF_GRID_MAPPING_POLAR = 'polar_stereographic'
CF_GRID_MAPPING_ROTATED_LAT_LON = 'rotated_latitude_longitude'
CF_GRID_MAPPING_STEREO = 'stereographic'
CF_GRID_MAPPING_TRANSVERSE = 'transverse_mercator'
CF_GRID_MAPPING_VERTICAL = 'vertical_perspective'
CF_GRID_MAPPING_GEOSTATIONARY = 'geostationary'
CF_ATTR_AXIS = 'axis'
CF_ATTR_BOUNDS = 'bounds'
CF_ATTR_CALENDAR = 'calendar'
CF_ATTR_CLIMATOLOGY = 'climatology'
CF_ATTR_GRID_INVERSE_FLATTENING = 'inverse_flattening'
CF_ATTR_GRID_EARTH_RADIUS = 'earth_radius'
CF_ATTR_GRID_MAPPING_NAME = 'grid_mapping_name'
CF_ATTR_GRID_NORTH_POLE_LAT = 'grid_north_pole_latitude'
CF_ATTR_GRID_NORTH_POLE_LON = 'grid_north_pole_longitude'
CF_ATTR_GRID_NORTH_POLE_GRID_LON = 'north_pole_grid_longitude'
CF_ATTR_GRID_SEMI_MAJOR_AXIS = 'semi_major_axis'
CF_ATTR_GRID_SEMI_MINOR_AXIS = 'semi_minor_axis'
CF_ATTR_GRID_LAT_OF_PROJ_ORIGIN = 'latitude_of_projection_origin'
CF_ATTR_GRID_LON_OF_PROJ_ORIGIN = 'longitude_of_projection_origin'
CF_ATTR_GRID_STANDARD_PARALLEL = 'standard_parallel'
CF_ATTR_GRID_FALSE_EASTING = 'false_easting'
CF_ATTR_GRID_FALSE_NORTHING = 'false_northing'
CF_ATTR_GRID_SCALE_FACTOR_AT_PROJ_ORIGIN = 'scale_factor_at_projection_origin'
CF_ATTR_GRID_SCALE_FACTOR_AT_CENT_MERIDIAN = 'scale_factor_at_central_meridian'
CF_ATTR_GRID_LON_OF_CENT_MERIDIAN = 'longitude_of_central_meridian'
CF_ATTR_GRID_STANDARD_PARALLEL = 'standard_parallel'
CF_ATTR_GRID_PERSPECTIVE_HEIGHT = 'perspective_point_height'
CF_ATTR_GRID_SWEEP_ANGLE_AXIS = 'sweep_angle_axis'
CF_ATTR_POSITIVE = 'positive'
CF_ATTR_STD_NAME = 'standard_name'
CF_ATTR_LONG_NAME = 'long_name'
CF_ATTR_UNITS = 'units'
CF_ATTR_CELL_METHODS = 'cell_methods'
CF_VALUE_AXIS_X = 'x'
CF_VALUE_AXIS_Y = 'y'
CF_VALUE_AXIS_T = 't'
CF_VALUE_AXIS_Z = 'z'
CF_VALUE_POSITIVE = ['down', 'up']
CF_VALUE_STD_NAME_LAT = 'latitude'
CF_VALUE_STD_NAME_LON = 'longitude'
CF_VALUE_STD_NAME_GRID_LAT = 'grid_latitude'
CF_VALUE_STD_NAME_GRID_LON = 'grid_longitude'
CF_VALUE_STD_NAME_PROJ_X = 'projection_x_coordinate'
CF_VALUE_STD_NAME_PROJ_Y = 'projection_y_coordinate'
def build_cube_metadata(engine):
    """Add the standard meta data to the cube."""
    cf_var = engine.cf_var
    cube = engine.cube
    cube.var_name = cf_var.cf_name
    standard_name = getattr(cf_var, CF_ATTR_STD_NAME, None)
    long_name = getattr(cf_var, CF_ATTR_LONG_NAME, None)
    cube.long_name = long_name
    if standard_name is not None:
        try:
            cube.standard_name = _get_valid_standard_name(standard_name)
        except ValueError:
            if cube.long_name is not None:
                cube.attributes['invalid_standard_name'] = standard_name
            else:
                cube.long_name = standard_name
    attr_units = get_attr_units(cf_var, cube.attributes)
    cube.units = attr_units
    nc_att_cell_methods = getattr(cf_var, CF_ATTR_CELL_METHODS, None)
    with warnings.catch_warnings(record=True) as warning_records:
        cube.cell_methods = parse_cell_methods(nc_att_cell_methods)
    warning_records = [record for record in warning_records
                       if issubclass(record.category, UnknownCellMethodWarning)]
    if len(warning_records) > 0:
        warn_record = warning_records[0]
        name = '{}'.format(cf_var.cf_name)
        msg = warn_record.message.args[0]
        msg = msg.replace('variable', 'variable {!r}'.format(name))
        warnings.warn(message=msg, category=UnknownCellMethodWarning)
    for attr_name, attr_value in cf_var.cf_group.global_attributes.items():
        try:
            cube.attributes[str(attr_name)] = attr_value
        except ValueError as e:
            msg = 'Skipping global attribute {!r}: {}'
            warnings.warn(msg.format(attr_name, str(e)))
def _get_ellipsoid(cf_grid_var):
    """Return the ellipsoid definition."""
    major = getattr(cf_grid_var, CF_ATTR_GRID_SEMI_MAJOR_AXIS, None)
    minor = getattr(cf_grid_var, CF_ATTR_GRID_SEMI_MINOR_AXIS, None)
    inverse_flattening = getattr(cf_grid_var, CF_ATTR_GRID_INVERSE_FLATTENING, None)
    if major is not None and minor is not None:
        inverse_flattening = None
    if major is None and minor is None and inverse_flattening is None:
        major = getattr(cf_grid_var, CF_ATTR_GRID_EARTH_RADIUS, None)
    return major, minor, inverse_flattening
def build_coordinate_system(cf_grid_var):
    """Create a coordinate system from the CF-netCDF grid mapping variable."""
    major, minor, inverse_flattening = _get_ellipsoid(cf_grid_var)
    return iris.coord_systems.GeogCS(major, minor, inverse_flattening)
def build_rotated_coordinate_system(engine, cf_grid_var):
    """Create a rotated coordinate system from the CF-netCDF grid mapping variable."""
    major, minor, inverse_flattening = _get_ellipsoid(cf_grid_var)
    north_pole_latitude = getattr(cf_grid_var, CF_ATTR_GRID_NORTH_POLE_LAT, 90.0)
    north_pole_longitude = getattr(cf_grid_var, CF_ATTR_GRID_NORTH_POLE_LON, 0.0)
    if north_pole_latitude is None or north_pole_longitude is None:
        warnings.warn('Rotated pole position is not fully specified')
    north_pole_grid_lon = getattr(cf_grid_var, CF_ATTR_GRID_NORTH_POLE_GRID_LON, 0.0)
    ellipsoid = None
    if major is not None or minor is not None or inverse_flattening is not None:
        ellipsoid = iris.coord_systems.GeogCS(major, minor, inverse_flattening)
    rcs = iris.coord_systems.RotatedGeogCS(north_pole_latitude, north_pole_longitude,
                                           north_pole_grid_lon, ellipsoid)
    return rcs
def build_transverse_mercator_coordinate_system(engine, cf_grid_var):
    """
        Create a transverse Mercator coordinate system from the CF-netCDF
        grid mapping variable.

        """
    major, minor, inverse_flattening = _get_ellipsoid(cf_grid_var)
    latitude_of_projection_origin = getattr(
        cf_grid_var, CF_ATTR_GRID_LAT_OF_PROJ_ORIGIN, None)
    longitude_of_central_meridian = getattr(
        cf_grid_var, CF_ATTR_GRID_LON_OF_CENT_MERIDIAN, None)
    false_easting = getattr(
        cf_grid_var, CF_ATTR_GRID_FALSE_EASTING, None)
    false_northing = getattr(
        cf_grid_var, CF_ATTR_GRID_FALSE_NORTHING, None)
    scale_factor_at_central_meridian = getattr(
        cf_grid_var, CF_ATTR_GRID_SCALE_FACTOR_AT_CENT_MERIDIAN, None)
    if longitude_of_central_meridian is None:
        longitude_of_central_meridian = getattr(
            cf_grid_var, CF_ATTR_GRID_LON_OF_PROJ_ORIGIN, None)
    if scale_factor_at_central_meridian is None:
        scale_factor_at_central_meridian = getattr(
            cf_grid_var, CF_ATTR_GRID_SCALE_FACTOR_AT_PROJ_ORIGIN, None)
    ellipsoid = None
    if major is not None or minor is not None or \
                inverse_flattening is not None:
        ellipsoid = iris.coord_systems.GeogCS(major, minor,
                                              inverse_flattening)
    cs = iris.coord_systems.TransverseMercator(
        latitude_of_projection_origin, longitude_of_central_meridian,
        false_easting, false_northing, scale_factor_at_central_meridian,
        ellipsoid)
    return cs
def build_lambert_conformal_coordinate_system(engine, cf_grid_var):
    """
        Create a Lambert conformal conic coordinate system from the CF-netCDF
        grid mapping variable.

        """
    major, minor, inverse_flattening = _get_ellipsoid(cf_grid_var)
    latitude_of_projection_origin = getattr(
        cf_grid_var, CF_ATTR_GRID_LAT_OF_PROJ_ORIGIN, None)
    longitude_of_central_meridian = getattr(
        cf_grid_var, CF_ATTR_GRID_LON_OF_CENT_MERIDIAN, None)
    false_easting = getattr(
        cf_grid_var, CF_ATTR_GRID_FALSE_EASTING, None)
    false_northing = getattr(
        cf_grid_var, CF_ATTR_GRID_FALSE_NORTHING, None)
    standard_parallel = getattr(
        cf_grid_var, CF_ATTR_GRID_STANDARD_PARALLEL, None)
    ellipsoid = None
    if major is not None or minor is not None or \
                inverse_flattening is not None:
        ellipsoid = iris.coord_systems.GeogCS(major, minor,
                                              inverse_flattening)
    cs = iris.coord_systems.LambertConformal(
        latitude_of_projection_origin, longitude_of_central_meridian,
        false_easting, false_northing, standard_parallel,
        ellipsoid)
    return cs
def build_stereographic_coordinate_system(engine, cf_grid_var):
    """
        Create a stereographic coordinate system from the CF-netCDF
        grid mapping variable.

        """
    major, minor, inverse_flattening = _get_ellipsoid(cf_grid_var)
    latitude_of_projection_origin = getattr(
        cf_grid_var, CF_ATTR_GRID_LAT_OF_PROJ_ORIGIN, None)
    longitude_of_projection_origin = getattr(
        cf_grid_var, CF_ATTR_GRID_LON_OF_PROJ_ORIGIN, None)
    false_easting = getattr(
        cf_grid_var, CF_ATTR_GRID_FALSE_EASTING, None)
    false_northing = getattr(
        cf_grid_var, CF_ATTR_GRID_FALSE_NORTHING, None)
    ellipsoid = None
    if major is not None or minor is not None or \
                inverse_flattening is not None:
        ellipsoid = iris.coord_systems.GeogCS(major, minor,
                                              inverse_flattening)
    cs = iris.coord_systems.Stereographic(
        latitude_of_projection_origin, longitude_of_projection_origin,
        false_easting, false_northing,
        true_scale_lat=None,
        ellipsoid=ellipsoid)
    return cs
def build_mercator_coordinate_system(engine, cf_grid_var):
    """
        Create a Mercator coordinate system from the CF-netCDF
        grid mapping variable.

        """
    major, minor, inverse_flattening = _get_ellipsoid(cf_grid_var)
    longitude_of_projection_origin = getattr(
        cf_grid_var, CF_ATTR_GRID_LON_OF_PROJ_ORIGIN, None)
    ellipsoid = None
    if major is not None or minor is not None or \
                inverse_flattening is not None:
        ellipsoid = iris.coord_systems.GeogCS(major, minor,
                                              inverse_flattening)
    cs = iris.coord_systems.Mercator(
        longitude_of_projection_origin,
        ellipsoid=ellipsoid)
    return cs
def build_lambert_azimuthal_equal_area_coordinate_system(engine, cf_grid_var):
    """
        Create a lambert azimuthal equal area coordinate system from the CF-netCDF
        grid mapping variable.

        """
    major, minor, inverse_flattening = _get_ellipsoid(cf_grid_var)
    latitude_of_projection_origin = getattr(
        cf_grid_var, CF_ATTR_GRID_LAT_OF_PROJ_ORIGIN, None)
    longitude_of_projection_origin = getattr(
        cf_grid_var, CF_ATTR_GRID_LON_OF_PROJ_ORIGIN, None)
    false_easting = getattr(
        cf_grid_var, CF_ATTR_GRID_FALSE_EASTING, None)
    false_northing = getattr(
        cf_grid_var, CF_ATTR_GRID_FALSE_NORTHING, None)
    ellipsoid = None
    if major is not None or minor is not None or \
                inverse_flattening is not None:
        ellipsoid = iris.coord_systems.GeogCS(major, minor,
                                              inverse_flattening)
    cs = iris.coord_systems.LambertAzimuthalEqualArea(
        latitude_of_projection_origin, longitude_of_projection_origin,
        false_easting, false_northing, ellipsoid)
    return cs
def build_albers_equal_area_coordinate_system(engine, cf_grid_var):
    """
        Create a albers conical equal area coordinate system from the CF-netCDF
        grid mapping variable.

        """
    major, minor, inverse_flattening = _get_ellipsoid(cf_grid_var)
    latitude_of_projection_origin = getattr(
        cf_grid_var, CF_ATTR_GRID_LAT_OF_PROJ_ORIGIN, None)
    longitude_of_central_meridian = getattr(
        cf_grid_var, CF_ATTR_GRID_LON_OF_CENT_MERIDIAN, None)
    false_easting = getattr(
        cf_grid_var, CF_ATTR_GRID_FALSE_EASTING, None)
    false_northing = getattr(
        cf_grid_var, CF_ATTR_GRID_FALSE_NORTHING, None)
    standard_parallels = getattr(
        cf_grid_var, CF_ATTR_GRID_STANDARD_PARALLEL, None)
    ellipsoid = None
    if major is not None or minor is not None or \
                inverse_flattening is not None:
        ellipsoid = iris.coord_systems.GeogCS(major, minor,
                                              inverse_flattening)
    cs = iris.coord_systems.AlbersEqualArea(
        latitude_of_projection_origin, longitude_of_central_meridian,
        false_easting, false_northing, standard_parallels, ellipsoid)
    return cs
def build_vertical_perspective_coordinate_system(engine, cf_grid_var):
    """
        Create a vertical perspective coordinate system from the CF-netCDF
        grid mapping variable.

        """
    major, minor, inverse_flattening = _get_ellipsoid(cf_grid_var)
    latitude_of_projection_origin = getattr(
        cf_grid_var, CF_ATTR_GRID_LAT_OF_PROJ_ORIGIN, None)
    longitude_of_projection_origin = getattr(
        cf_grid_var, CF_ATTR_GRID_LON_OF_PROJ_ORIGIN, None)
    perspective_point_height = getattr(
        cf_grid_var, CF_ATTR_GRID_PERSPECTIVE_HEIGHT, None)
    false_easting = getattr(
        cf_grid_var, CF_ATTR_GRID_FALSE_EASTING, None)
    false_northing = getattr(
        cf_grid_var, CF_ATTR_GRID_FALSE_NORTHING, None)
    ellipsoid = None
    if major is not None or minor is not None or \
                inverse_flattening is not None:
        ellipsoid = iris.coord_systems.GeogCS(major, minor,
                                              inverse_flattening)
    cs = iris.coord_systems.VerticalPerspective(
        latitude_of_projection_origin, longitude_of_projection_origin,
        perspective_point_height, false_easting, false_northing, ellipsoid)
    return cs
def build_geostationary_coordinate_system(engine, cf_grid_var):
    """
        Create a geostationary coordinate system from the CF-netCDF
        grid mapping variable.

        """
    major, minor, inverse_flattening = _get_ellipsoid(cf_grid_var)
    latitude_of_projection_origin = getattr(
        cf_grid_var, CF_ATTR_GRID_LAT_OF_PROJ_ORIGIN, None)
    longitude_of_projection_origin = getattr(
        cf_grid_var, CF_ATTR_GRID_LON_OF_PROJ_ORIGIN, None)
    perspective_point_height = getattr(
        cf_grid_var, CF_ATTR_GRID_PERSPECTIVE_HEIGHT, None)
    false_easting = getattr(
        cf_grid_var, CF_ATTR_GRID_FALSE_EASTING, None)
    false_northing = getattr(
        cf_grid_var, CF_ATTR_GRID_FALSE_NORTHING, None)
    sweep_angle_axis = getattr(
        cf_grid_var, CF_ATTR_GRID_SWEEP_ANGLE_AXIS, None)
    ellipsoid = None
    if major is not None or minor is not None or \
                inverse_flattening is not None:
        ellipsoid = iris.coord_systems.GeogCS(major, minor,
                                              inverse_flattening)
    cs = iris.coord_systems.Geostationary(
        latitude_of_projection_origin, longitude_of_projection_origin,
        perspective_point_height, sweep_angle_axis, false_easting,
        false_northing, ellipsoid)
    return cs
def get_attr_units(cf_var, attributes):
    attr_units = getattr(cf_var, CF_ATTR_UNITS, cf_units._UNIT_DIMENSIONLESS)
    if not attr_units:
        attr_units = '1'
    if attr_units in UD_UNITS_LAT or attr_units in UD_UNITS_LON:
        attr_units = 'degrees'
    try:
        cf_units.as_unit(attr_units)
    except ValueError:
        msg = u'Ignoring netCDF variable {!r} invalid units {!r}'.format(
            cf_var.cf_name, attr_units)
        warnings.warn(msg)
        attributes['invalid_units'] = attr_units
        attr_units = cf_units._UNKNOWN_UNIT_STRING
    if np.issubdtype(cf_var.dtype, np.str_):
        attr_units = cf_units._NO_UNIT_STRING
    if cf_units.as_unit(attr_units).is_time_reference():
        attr_calendar = getattr(cf_var, CF_ATTR_CALENDAR, None)
        if attr_calendar:
            attr_units = cf_units.Unit(attr_units, calendar=attr_calendar)
    return attr_units
def get_names(cf_coord_var, coord_name, attributes):
    """Determine the standard_name, long_name and var_name attributes."""
    standard_name = getattr(cf_coord_var, CF_ATTR_STD_NAME, None)
    long_name = getattr(cf_coord_var, CF_ATTR_LONG_NAME, None)
    cf_name = str(cf_coord_var.cf_name)
    if standard_name is not None:
        try:
            standard_name = _get_valid_standard_name(standard_name)
        except ValueError:
            if long_name is not None:
                attributes['invalid_standard_name'] = standard_name
                if coord_name is not None:
                    standard_name = coord_name
                else:
                    standard_name = None
            else:
                if coord_name is not None:
                    attributes['invalid_standard_name'] = standard_name
                    standard_name = coord_name
                else:
                    standard_name = None
    else:
        if coord_name is not None:
            standard_name = coord_name
    if standard_name is None:
        if cf_name in iris.std_names.STD_NAMES:
            standard_name = cf_name
    return (standard_name, long_name, cf_name)
def get_cf_bounds_var(cf_coord_var):
    """
        Return the CF variable representing the bounds of a coordinate
        variable.

        """
    attr_bounds = getattr(cf_coord_var, CF_ATTR_BOUNDS, None)
    attr_climatology = getattr(cf_coord_var, CF_ATTR_CLIMATOLOGY, None)
    cf_bounds_var = None
    climatological = False
    if attr_bounds is not None:
        bounds_vars = cf_coord_var.cf_group.bounds
        if attr_bounds in bounds_vars:
            cf_bounds_var = bounds_vars[attr_bounds]
    elif attr_climatology is not None:
        climatology_vars = cf_coord_var.cf_group.climatology
        if attr_climatology in climatology_vars:
            cf_bounds_var = climatology_vars[attr_climatology]
            climatological = True
    if attr_bounds is not None and attr_climatology is not None:
        warnings.warn('Ignoring climatology in favour of bounds attribute '
                      'on NetCDF variable {!r}.'.format(
                      cf_coord_var.cf_name))
    return cf_bounds_var, climatological
def reorder_bounds_data(bounds_data, cf_bounds_var, cf_coord_var):
    """
        Return a bounds_data array with the vertex dimension as the most
        rapidly varying.

        .. note::

            This function assumes the dimension names of the coordinate
            variable match those of the bounds variable in order to determine
            which is the vertex dimension.


        """
    vertex_dim_names = set(cf_bounds_var.dimensions).difference(
        cf_coord_var.dimensions)
    if len(vertex_dim_names) != 1:
        msg = 'Too many dimension names differ between coordinate ' \
                  'variable {!r} and the bounds variable {!r}. ' \
                  'Expected 1, got {}.'
        raise ValueError(msg.format(str(cf_coord_var.cf_name),
                                    str(cf_bounds_var.cf_name),
                                    len(vertex_dim_names)))
    vertex_dim = cf_bounds_var.dimensions.index(*vertex_dim_names)
    bounds_data = np.rollaxis(bounds_data.view(), vertex_dim,
                              len(bounds_data.shape))
    return bounds_data
def build_dimension_coordinate(engine, cf_coord_var, coord_name=None, coord_system=None):
    """Create a dimension coordinate (DimCoord) and add it to the cube."""
    cf_var = engine.cf_var
    cube = engine.cube
    attributes = {}
    attr_units = get_attr_units(cf_coord_var, attributes)
    points_data = cf_coord_var[:]
    if ma.is_masked(points_data):
        points_data = ma.filled(points_data)
        msg = 'Gracefully filling {!r} dimension coordinate masked points'
        warnings.warn(msg.format(str(cf_coord_var.cf_name)))
    cf_bounds_var, climatological = get_cf_bounds_var(
        cf_coord_var)
    if cf_bounds_var is not None:
        bounds_data = cf_bounds_var[:]
        if ma.is_masked(bounds_data):
            bounds_data = ma.filled(bounds_data)
            msg = 'Gracefully filling {!r} dimension coordinate masked bounds'
            warnings.warn(msg.format(str(cf_coord_var.cf_name)))
        if cf_bounds_var.shape[:-1] != cf_coord_var.shape:
            bounds_data = reorder_bounds_data(bounds_data, cf_bounds_var,
                                              cf_coord_var)
    else:
        bounds_data = None
    circular = False
    if points_data.ndim == 1 and coord_name in [CF_VALUE_STD_NAME_LON, CF_VALUE_STD_NAME_GRID_LON] \
            and cf_units.Unit(attr_units) in [cf_units.Unit('radians'), cf_units.Unit('degrees')]:
            modulus_value = cf_units.Unit(attr_units).modulus
            circular = iris.util._is_circular(points_data, modulus_value, bounds=bounds_data)
    common_dims = [dim for dim in cf_coord_var.dimensions
                   if dim in cf_var.dimensions]
    data_dims = None
    if common_dims:
        data_dims = [cf_var.dimensions.index(dim) for dim in common_dims]
    standard_name, long_name, var_name = get_names(cf_coord_var, coord_name, attributes)
    try:
        coord = iris.coords.DimCoord(points_data,
                                     standard_name=standard_name,
                                     long_name=long_name,
                                     var_name=var_name,
                                     units=attr_units,
                                     bounds=bounds_data,
                                     attributes=attributes,
                                     coord_system=coord_system,
                                     circular=circular,
                                     climatological=
                                         climatological)
    except ValueError as e_msg:
        coord = iris.coords.AuxCoord(points_data,
                                     standard_name=standard_name,
                                     long_name=long_name,
                                     var_name=var_name,
                                     units=attr_units,
                                     bounds=bounds_data,
                                     attributes=attributes,
                                     coord_system=coord_system,
                                     climatological=
                                         climatological)
        cube.add_aux_coord(coord, data_dims)
        msg = 'Failed to create {name!r} dimension coordinate: {error}\n' \
                  'Gracefully creating {name!r} auxiliary coordinate instead.'
        warnings.warn(msg.format(name=str(cf_coord_var.cf_name),
                                 error=e_msg))
    else:
        if data_dims:
            cube.add_dim_coord(coord, data_dims)
        else:
            cube.add_aux_coord(coord, data_dims)
    engine.provides['coordinates'].append((coord, cf_coord_var.cf_name))
def build_auxiliary_coordinate(engine, cf_coord_var, coord_name=None, coord_system=None):
    """Create an auxiliary coordinate (AuxCoord) and add it to the cube."""
    cf_var = engine.cf_var
    cube = engine.cube
    attributes = {}
    attr_units = get_attr_units(cf_coord_var, attributes)
    if isinstance(cf_coord_var, cf.CFLabelVariable):
        points_data = cf_coord_var.cf_label_data(cf_var)
    else:
        points_data = _get_cf_var_data(cf_coord_var, engine.filename)
    cf_bounds_var, climatological = get_cf_bounds_var(
        cf_coord_var)
    if cf_bounds_var is not None:
        bounds_data = _get_cf_var_data(cf_bounds_var, engine.filename)
        if cf_bounds_var.shape[:-1] != cf_coord_var.shape:
            bounds_data = np.asarray(bounds_data)
            bounds_data = reorder_bounds_data(bounds_data, cf_bounds_var,
                                              cf_coord_var)
    else:
        bounds_data = None
    common_dims = [dim for dim in cf_coord_var.dimensions
                   if dim in cf_var.dimensions]
    data_dims = None
    if common_dims:
        data_dims = [cf_var.dimensions.index(dim) for dim in common_dims]
    standard_name, long_name, var_name = get_names(cf_coord_var, coord_name, attributes)
    coord = iris.coords.AuxCoord(points_data,
                                 standard_name=standard_name,
                                 long_name=long_name,
                                 var_name=var_name,
                                 units=attr_units,
                                 bounds=bounds_data,
                                 attributes=attributes,
                                 coord_system=coord_system,
                                 climatological=
                                     climatological)
    cube.add_aux_coord(coord, data_dims)
    engine.provides['coordinates'].append((coord, cf_coord_var.cf_name))
def build_cell_measures(engine, cf_cm_attr, coord_name=None):
    """Create a CellMeasure instance and add it to the cube."""
    cf_var = engine.cf_var
    cube = engine.cube
    attributes = {}
    attr_units = get_attr_units(cf_cm_attr, attributes)
    data = _get_cf_var_data(cf_cm_attr, engine.filename)
    common_dims = [dim for dim in cf_cm_attr.dimensions
                   if dim in cf_var.dimensions]
    data_dims = None
    if common_dims:
        data_dims = [cf_var.dimensions.index(dim) for dim in common_dims]
    standard_name, long_name, var_name = get_names(cf_cm_attr, coord_name, attributes)
    measure = cf_cm_attr.cf_measure
    cell_measure = iris.coords.CellMeasure(data,
                                           standard_name=standard_name,
                                           long_name=long_name,
                                           var_name=var_name,
                                           units=attr_units,
                                           attributes=attributes,
                                           measure=measure)
    cube.add_cell_measure(cell_measure, data_dims)
def _is_lat_lon(cf_var, ud_units, std_name, std_name_grid, axis_name, prefixes):
    """
        Determine whether the CF coordinate variable is a latitude/longitude variable.

        Ref: [CF] Section 4.1 Latitude Coordinate.
             [CF] Section 4.2 Longitude Coordinate.

        """
    is_valid = False
    attr_units = getattr(cf_var, CF_ATTR_UNITS, None)
    if attr_units is not None:
        attr_units = attr_units.lower()
        is_valid = attr_units in ud_units
        if attr_units == 'degrees':
            attr_std_name = getattr(cf_var, CF_ATTR_STD_NAME, None)
            if attr_std_name is not None:
                is_valid = attr_std_name.lower() == std_name_grid
            else:
                is_valid = False
                attr_axis = getattr(cf_var, CF_ATTR_AXIS, None)
                if attr_axis is not None:
                    is_valid = attr_axis.lower() == axis_name
    else:
        attr_std_name = getattr(cf_var, CF_ATTR_STD_NAME, None)
        if attr_std_name is not None:
            attr_std_name = attr_std_name.lower()
            is_valid = attr_std_name in [std_name, std_name_grid]
            if not is_valid:
                is_valid = any([attr_std_name.startswith(prefix) for prefix in prefixes])
        else:
            attr_axis = getattr(cf_var, CF_ATTR_AXIS, None)
            if attr_axis is not None:
                is_valid = attr_axis.lower() == axis_name
    return is_valid
def is_latitude(engine, cf_name):
    """Determine whether the CF coordinate variable is a latitude variable."""
    cf_var = engine.cf_var.cf_group[cf_name]
    return _is_lat_lon(cf_var, UD_UNITS_LAT, CF_VALUE_STD_NAME_LAT,
                       CF_VALUE_STD_NAME_GRID_LAT, CF_VALUE_AXIS_Y, ['lat', 'rlat'])
def is_longitude(engine, cf_name):
    """Determine whether the CF coordinate variable is a longitude variable."""
    cf_var = engine.cf_var.cf_group[cf_name]
    return _is_lat_lon(cf_var, UD_UNITS_LON, CF_VALUE_STD_NAME_LON,
                       CF_VALUE_STD_NAME_GRID_LON, CF_VALUE_AXIS_X, ['lon', 'rlon'])
def is_projection_x_coordinate(engine, cf_name):
    """
        Determine whether the CF coordinate variable is a
        projection_x_coordinate variable.

        """
    cf_var = engine.cf_var.cf_group[cf_name]
    attr_name = getattr(cf_var, CF_ATTR_STD_NAME, None) or \
            getattr(cf_var, CF_ATTR_LONG_NAME, None)
    return attr_name == CF_VALUE_STD_NAME_PROJ_X
def is_projection_y_coordinate(engine, cf_name):
    """
        Determine whether the CF coordinate variable is a
        projection_y_coordinate variable.

        """
    cf_var = engine.cf_var.cf_group[cf_name]
    attr_name = getattr(cf_var, CF_ATTR_STD_NAME, None) or \
            getattr(cf_var, CF_ATTR_LONG_NAME, None)
    return attr_name == CF_VALUE_STD_NAME_PROJ_Y
def is_time(engine, cf_name):
    """
        Determine whether the CF coordinate variable is a time variable.

        Ref: [CF] Section 4.4 Time Coordinate.

        """
    is_valid = False
    cf_var = engine.cf_var.cf_group[cf_name]
    attr_units = getattr(cf_var, CF_ATTR_UNITS, None)
    attr_std_name = getattr(cf_var, CF_ATTR_STD_NAME, None)
    attr_axis = getattr(cf_var, CF_ATTR_AXIS, '')
    try:
        is_time_reference = cf_units.Unit(attr_units or 1).is_time_reference()
    except ValueError:
        is_time_reference = False
    return is_time_reference and (attr_std_name=='time' or attr_axis.lower()==CF_VALUE_AXIS_T)
def is_time_period(engine, cf_name):
    """Determine whether the CF coordinate variable represents a time period."""
    is_valid = False
    cf_var = engine.cf_var.cf_group[cf_name]
    attr_units = getattr(cf_var, CF_ATTR_UNITS, None)
    if attr_units is not None:
        try:
            is_valid = cf_units.is_time(attr_units)
        except ValueError:
            is_valid = False
    return is_valid
def is_grid_mapping(engine, cf_name, grid_mapping):
    """Determine whether the CF grid mapping variable is of the appropriate type."""
    is_valid = False
    cf_var = engine.cf_var.cf_group[cf_name]
    attr_mapping_name = getattr(cf_var, CF_ATTR_GRID_MAPPING_NAME, None)
    if attr_mapping_name is not None:
        is_valid = attr_mapping_name.lower() == grid_mapping
    return is_valid
def _is_rotated(engine, cf_name, cf_attr_value):
    """Determine whether the CF coordinate variable is rotated."""
    is_valid = False
    cf_var = engine.cf_var.cf_group[cf_name]
    attr_std_name = getattr(cf_var, CF_ATTR_STD_NAME, None)
    if attr_std_name is not None:
        is_valid = attr_std_name.lower() == cf_attr_value
    else:
        attr_units = getattr(cf_var, CF_ATTR_UNITS, None)
        if attr_units is not None:
            is_valid = attr_units.lower() == 'degrees'
    return is_valid
def is_rotated_latitude(engine, cf_name):
    """Determine whether the CF coodinate variable is rotated latitude."""
    return _is_rotated(engine, cf_name, CF_VALUE_STD_NAME_GRID_LAT)
def is_rotated_longitude(engine, cf_name):
    """Determine whether the CF coordinate variable is rotated longitude."""
    return _is_rotated(engine, cf_name, CF_VALUE_STD_NAME_GRID_LON)
def has_supported_mercator_parameters(engine, cf_name):
    """Determine whether the CF grid mapping variable has the supported
        values for the parameters of the Mercator projection."""
    is_valid = True
    cf_grid_var = engine.cf_var.cf_group[cf_name]
    false_easting = getattr(
        cf_grid_var, CF_ATTR_GRID_FALSE_EASTING, None)
    false_northing = getattr(
        cf_grid_var, CF_ATTR_GRID_FALSE_NORTHING, None)
    scale_factor_at_projection_origin = getattr(
        cf_grid_var, CF_ATTR_GRID_SCALE_FACTOR_AT_PROJ_ORIGIN, None)
    standard_parallel = getattr(
        cf_grid_var, CF_ATTR_GRID_STANDARD_PARALLEL, None)
    if false_easting is not None and \
                false_easting != 0:
        warnings.warn('False eastings other than 0.0 not yet supported '
                      'for Mercator projections')
        is_valid = False
    if false_northing is not None and \
                false_northing != 0:
        warnings.warn('False northings other than 0.0 not yet supported '
                      'for Mercator projections')
        is_valid = False
    if scale_factor_at_projection_origin is not None and \
                scale_factor_at_projection_origin != 1:
        warnings.warn('Scale factors other than 1.0 not yet supported for '
                      'Mercator projections')
        is_valid = False
    if standard_parallel is not None and \
                standard_parallel != 0:
        warnings.warn('Standard parallels other than 0.0 not yet '
                      'supported for Mercator projections')
        is_valid = False
    return is_valid
def has_supported_stereographic_parameters(engine, cf_name):
    """Determine whether the CF grid mapping variable has a value of 1.0
        for the scale_factor_at_projection_origin attribute."""
    is_valid = True
    cf_grid_var = engine.cf_var.cf_group[cf_name]
    scale_factor_at_projection_origin = getattr(
        cf_grid_var, CF_ATTR_GRID_SCALE_FACTOR_AT_PROJ_ORIGIN, None)
    if scale_factor_at_projection_origin is not None and \
                scale_factor_at_projection_origin != 1:
        warnings.warn('Scale factors other than 1.0 not yet supported for '
                      'stereographic projections')
        is_valid = False
    return is_valid
def _parse_cell_methods(cf_var_name, nc_cell_methods):
    """Parse the CF cell_methods attribute string."""
    cell_methods = []
    if nc_cell_methods is not None:
        for m in CM_PARSE.finditer(nc_cell_methods):
            d = m.groupdict()
            method = d[CM_METHOD]
            method = method.strip()
            method_words = method.split()
            if method_words[0].lower() not in CM_KNOWN_METHODS:
                msg = 'NetCDF variable {!r} contains unknown cell ' \
                          'method {!r}'
                warnings.warn(msg.format('{}'.format(cf_var_name),
                                         '{}'.format(method_words[0])))
            d[CM_METHOD] = method
            name = d[CM_NAME]
            name = name.replace(' ', '')
            name = name.rstrip(':')
            d[CM_NAME] = tuple([n for n in name.split(':')])
            interval = []
            comment = []
            if d[CM_EXTRA] is not None:
                d[CM_EXTRA] = d[CM_EXTRA].replace('comment:', '<<comment>><<:>>')
                d[CM_EXTRA] = d[CM_EXTRA].replace('interval:', '<<interval>><<:>>')
                d[CM_EXTRA] = d[CM_EXTRA].split('<<:>>')
                if len(d[CM_EXTRA]) == 1:
                    comment.extend(d[CM_EXTRA])
                else:
                    next_field_type = comment
                    for field in d[CM_EXTRA]:
                        field_type = next_field_type
                        index = field.rfind('<<interval>>')
                        if index == 0:
                            next_field_type = interval
                            continue
                        elif index > 0:
                            next_field_type = interval
                        else:
                            index = field.rfind('<<comment>>')
                            if index == 0:
                                next_field_type = comment
                                continue
                            elif index > 0:
                                next_field_type = comment
                        if index != -1:
                            field = field[:index]
                        field_type.append(field.strip())
            if len(interval):
                if len(d[CM_NAME]) != len(interval) and len(interval) == 1:
                    interval = interval*len(d[CM_NAME])
            if len(comment):
                if len(d[CM_NAME]) != len(comment) and len(comment) == 1:
                    comment = comment*len(d[CM_NAME])
            d[CM_INTERVAL] = tuple(interval)
            d[CM_COMMENT] = tuple(comment)
            cell_methods.append(iris.coords.CellMethod(d[CM_METHOD], coords=d[CM_NAME], intervals=d[CM_INTERVAL], comments=d[CM_COMMENT]))
    return tuple(cell_methods)

Krb_filename = '../fc_rules_cf.krb'
Krb_lineno_map = (
    ((12, 12), (26, 26)),
    ((13, 13), (27, 27)),
    ((22, 26), (40, 40)),
    ((27, 27), (41, 41)),
    ((28, 28), (43, 43)),
    ((29, 29), (44, 44)),
    ((30, 30), (45, 45)),
    ((31, 33), (46, 46)),
    ((34, 34), (47, 47)),
    ((43, 47), (60, 60)),
    ((48, 48), (61, 61)),
    ((49, 49), (63, 63)),
    ((50, 50), (64, 64)),
    ((51, 51), (65, 65)),
    ((52, 54), (66, 66)),
    ((55, 55), (67, 67)),
    ((64, 68), (79, 79)),
    ((69, 69), (80, 80)),
    ((70, 70), (82, 82)),
    ((71, 71), (83, 83)),
    ((72, 72), (84, 84)),
    ((73, 75), (85, 85)),
    ((76, 76), (86, 86)),
    ((85, 89), (99, 99)),
    ((90, 90), (100, 100)),
    ((91, 91), (101, 101)),
    ((92, 92), (103, 103)),
    ((93, 93), (104, 104)),
    ((94, 94), (105, 105)),
    ((95, 97), (106, 106)),
    ((98, 98), (107, 107)),
    ((107, 111), (120, 120)),
    ((112, 112), (121, 121)),
    ((113, 113), (122, 122)),
    ((114, 114), (124, 124)),
    ((115, 115), (125, 125)),
    ((116, 116), (126, 126)),
    ((117, 119), (127, 127)),
    ((120, 120), (128, 128)),
    ((129, 133), (140, 140)),
    ((134, 134), (141, 141)),
    ((135, 135), (143, 143)),
    ((136, 136), (144, 144)),
    ((137, 137), (145, 145)),
    ((138, 140), (146, 146)),
    ((141, 141), (147, 147)),
    ((150, 154), (159, 159)),
    ((155, 155), (160, 160)),
    ((156, 156), (162, 162)),
    ((157, 157), (163, 163)),
    ((158, 158), (164, 164)),
    ((159, 161), (165, 165)),
    ((162, 162), (166, 166)),
    ((171, 175), (178, 178)),
    ((176, 176), (179, 179)),
    ((177, 177), (181, 181)),
    ((178, 178), (182, 182)),
    ((179, 179), (183, 183)),
    ((180, 182), (184, 184)),
    ((183, 183), (185, 185)),
    ((192, 196), (197, 197)),
    ((197, 197), (198, 198)),
    ((198, 198), (200, 200)),
    ((199, 200), (201, 202)),
    ((201, 201), (203, 203)),
    ((202, 204), (204, 204)),
    ((205, 205), (205, 205)),
    ((214, 218), (217, 217)),
    ((219, 220), (218, 219)),
    ((221, 221), (221, 221)),
    ((222, 223), (222, 223)),
    ((224, 224), (224, 224)),
    ((225, 227), (225, 225)),
    ((228, 228), (226, 226)),
    ((237, 241), (239, 239)),
    ((242, 242), (240, 240)),
    ((243, 246), (242, 242)),
    ((247, 247), (243, 243)),
    ((256, 260), (256, 256)),
    ((261, 261), (257, 257)),
    ((262, 265), (259, 259)),
    ((266, 266), (260, 260)),
    ((275, 279), (273, 273)),
    ((280, 280), (274, 274)),
    ((281, 284), (276, 276)),
    ((285, 285), (277, 277)),
    ((294, 298), (290, 290)),
    ((299, 299), (291, 291)),
    ((300, 303), (293, 293)),
    ((304, 304), (294, 294)),
    ((313, 317), (307, 307)),
    ((318, 318), (308, 308)),
    ((319, 322), (310, 310)),
    ((323, 323), (311, 311)),
    ((332, 336), (325, 325)),
    ((337, 337), (326, 326)),
    ((338, 341), (328, 328)),
    ((342, 342), (329, 329)),
    ((351, 355), (341, 341)),
    ((356, 356), (343, 343)),
    ((357, 357), (344, 344)),
    ((358, 358), (345, 345)),
    ((367, 371), (359, 359)),
    ((372, 372), (360, 360)),
    ((373, 373), (362, 362)),
    ((374, 374), (363, 363)),
    ((375, 375), (364, 364)),
    ((384, 388), (377, 377)),
    ((389, 389), (378, 378)),
    ((390, 390), (380, 380)),
    ((391, 391), (381, 381)),
    ((392, 392), (382, 382)),
    ((401, 405), (395, 395)),
    ((406, 406), (396, 396)),
    ((407, 407), (397, 397)),
    ((408, 408), (399, 399)),
    ((409, 410), (400, 401)),
    ((411, 411), (402, 402)),
    ((420, 424), (415, 415)),
    ((425, 425), (416, 416)),
    ((426, 426), (417, 417)),
    ((427, 427), (419, 419)),
    ((428, 429), (420, 421)),
    ((430, 430), (422, 422)),
    ((439, 443), (435, 435)),
    ((444, 444), (436, 436)),
    ((445, 445), (437, 437)),
    ((446, 446), (439, 439)),
    ((447, 448), (440, 441)),
    ((449, 449), (442, 442)),
    ((458, 462), (455, 455)),
    ((463, 463), (456, 456)),
    ((464, 464), (457, 457)),
    ((465, 465), (459, 459)),
    ((466, 467), (460, 461)),
    ((468, 468), (462, 462)),
    ((477, 481), (475, 475)),
    ((482, 482), (476, 476)),
    ((483, 483), (477, 477)),
    ((484, 484), (478, 478)),
    ((485, 485), (479, 479)),
    ((486, 486), (481, 481)),
    ((487, 487), (482, 482)),
    ((488, 488), (483, 483)),
    ((497, 501), (494, 494)),
    ((502, 502), (496, 496)),
    ((503, 503), (497, 497)),
    ((504, 504), (498, 498)),
    ((513, 517), (511, 511)),
    ((518, 522), (512, 512)),
    ((523, 523), (513, 513)),
    ((524, 524), (515, 515)),
    ((525, 527), (516, 518)),
    ((528, 528), (519, 519)),
    ((537, 541), (532, 532)),
    ((542, 546), (533, 533)),
    ((547, 547), (534, 534)),
    ((548, 548), (536, 536)),
    ((549, 551), (537, 539)),
    ((552, 552), (540, 540)),
    ((561, 565), (553, 553)),
    ((566, 570), (554, 554)),
    ((571, 571), (555, 555)),
    ((572, 572), (557, 557)),
    ((573, 575), (558, 560)),
    ((576, 576), (561, 561)),
    ((585, 589), (574, 574)),
    ((590, 594), (575, 575)),
    ((595, 595), (576, 576)),
    ((596, 596), (578, 578)),
    ((597, 599), (579, 581)),
    ((600, 600), (582, 582)),
    ((609, 613), (595, 595)),
    ((615, 618), (597, 597)),
    ((623, 626), (599, 599)),
    ((630, 630), (601, 601)),
    ((631, 633), (602, 604)),
    ((634, 634), (605, 605)),
    ((643, 647), (618, 618)),
    ((649, 652), (620, 620)),
    ((657, 660), (622, 622)),
    ((664, 664), (624, 624)),
    ((665, 667), (625, 627)),
    ((668, 668), (628, 628)),
    ((677, 681), (641, 641)),
    ((682, 686), (642, 642)),
    ((687, 687), (644, 644)),
    ((688, 690), (645, 647)),
    ((691, 691), (648, 648)),
    ((700, 704), (661, 661)),
    ((705, 709), (662, 662)),
    ((710, 710), (664, 664)),
    ((711, 713), (665, 667)),
    ((714, 714), (668, 668)),
    ((723, 727), (680, 680)),
    ((728, 732), (681, 681)),
    ((733, 733), (683, 683)),
    ((734, 736), (684, 686)),
    ((737, 737), (687, 687)),
    ((746, 750), (700, 700)),
    ((751, 755), (701, 701)),
    ((756, 756), (703, 703)),
    ((757, 759), (704, 706)),
    ((760, 760), (707, 707)),
    ((769, 773), (720, 720)),
    ((774, 778), (721, 721)),
    ((779, 779), (723, 723)),
    ((780, 782), (724, 726)),
    ((783, 783), (727, 727)),
    ((792, 796), (739, 739)),
    ((797, 801), (740, 740)),
    ((802, 802), (742, 742)),
    ((803, 805), (743, 745)),
    ((806, 806), (746, 746)),
    ((815, 819), (758, 758)),
    ((820, 824), (759, 759)),
    ((825, 825), (761, 761)),
    ((826, 828), (762, 764)),
    ((829, 829), (765, 765)),
    ((838, 842), (777, 777)),
    ((843, 847), (778, 778)),
    ((848, 848), (780, 780)),
    ((849, 851), (781, 783)),
    ((852, 852), (784, 784)),
    ((861, 865), (797, 797)),
    ((866, 870), (798, 798)),
    ((871, 871), (800, 800)),
    ((872, 874), (801, 803)),
    ((875, 875), (804, 804)),
    ((884, 888), (817, 817)),
    ((889, 893), (818, 818)),
    ((894, 894), (820, 820)),
    ((895, 897), (821, 823)),
    ((898, 898), (824, 824)),
    ((907, 911), (836, 836)),
    ((912, 916), (837, 837)),
    ((917, 917), (839, 839)),
    ((918, 920), (840, 842)),
    ((921, 921), (843, 843)),
    ((930, 934), (856, 856)),
    ((935, 939), (857, 857)),
    ((940, 940), (859, 859)),
    ((941, 943), (860, 862)),
    ((944, 944), (863, 863)),
    ((953, 957), (875, 875)),
    ((958, 962), (876, 876)),
    ((963, 963), (878, 878)),
    ((964, 966), (879, 881)),
    ((967, 967), (882, 882)),
    ((976, 980), (895, 895)),
    ((981, 985), (896, 896)),
    ((986, 986), (898, 898)),
    ((987, 989), (899, 901)),
    ((990, 990), (902, 902)),
    ((999, 1003), (914, 914)),
    ((1004, 1008), (915, 915)),
    ((1009, 1009), (917, 917)),
    ((1010, 1012), (918, 920)),
    ((1013, 1013), (921, 921)),
    ((1022, 1026), (934, 934)),
    ((1027, 1031), (935, 935)),
    ((1032, 1032), (937, 937)),
    ((1033, 1035), (938, 940)),
    ((1036, 1036), (941, 941)),
    ((1045, 1049), (953, 953)),
    ((1050, 1050), (955, 955)),
    ((1051, 1051), (956, 956)),
    ((1052, 1052), (957, 957)),
    ((1061, 1065), (969, 969)),
    ((1066, 1066), (971, 971)),
    ((1067, 1067), (972, 972)),
    ((1068, 1068), (973, 973)),
    ((1077, 1081), (986, 986)),
    ((1083, 1086), (988, 988)),
    ((1090, 1090), (990, 990)),
    ((1091, 1091), (991, 991)),
    ((1092, 1095), (992, 992)),
    ((1096, 1096), (993, 993)),
    ((1105, 1105), (1007, 1007)),
    ((1106, 1106), (1009, 1009)),
    ((1107, 1107), (1010, 1010)),
    ((1108, 1108), (1011, 1011)),
    ((1117, 1117), (1024, 1024)),
    ((1118, 1118), (1026, 1026)),
    ((1119, 1119), (1027, 1027)),
    ((1120, 1120), (1028, 1028)),
    ((1129, 1133), (1041, 1041)),
    ((1134, 1134), (1042, 1042)),
    ((1135, 1135), (1044, 1044)),
    ((1136, 1137), (1045, 1045)),
    ((1138, 1138), (1046, 1046)),
    ((1147, 1151), (1058, 1058)),
    ((1152, 1152), (1059, 1059)),
    ((1153, 1153), (1061, 1061)),
    ((1154, 1155), (1062, 1062)),
    ((1156, 1156), (1063, 1063)),
    ((1165, 1169), (1075, 1075)),
    ((1170, 1170), (1076, 1076)),
    ((1171, 1171), (1078, 1078)),
    ((1172, 1173), (1079, 1079)),
    ((1174, 1174), (1080, 1080)),
    ((1183, 1187), (1092, 1092)),
    ((1188, 1188), (1093, 1093)),
    ((1189, 1189), (1095, 1095)),
    ((1190, 1191), (1096, 1096)),
    ((1192, 1192), (1097, 1097)),
    ((1201, 1205), (1109, 1109)),
    ((1206, 1206), (1110, 1110)),
    ((1207, 1207), (1112, 1112)),
    ((1208, 1209), (1113, 1113)),
    ((1210, 1210), (1114, 1114)),
    ((1219, 1223), (1126, 1126)),
    ((1224, 1224), (1127, 1127)),
    ((1225, 1225), (1129, 1129)),
    ((1226, 1227), (1130, 1130)),
    ((1228, 1228), (1131, 1131)),
    ((1237, 1241), (1143, 1143)),
    ((1242, 1242), (1144, 1144)),
    ((1243, 1243), (1146, 1146)),
    ((1244, 1245), (1147, 1147)),
    ((1246, 1246), (1148, 1148)),
    ((1255, 1259), (1160, 1160)),
    ((1260, 1264), (1161, 1161)),
    ((1265, 1265), (1163, 1163)),
    ((1266, 1266), (1164, 1164)),
)
