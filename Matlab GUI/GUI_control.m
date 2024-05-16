function GUI_control()
    % 创建图形窗口和控件
    fig = figure('Name', 'Trigonometric Calculator', 'Position', [100, 100, 600, 400]);
   
    % 选择输出模式为幅度或角度, mode =1 时显示弧度， =2 时显示角度
    show = uicontrol('Style', 'edit', 'Position', [380, 360, 50, 20]);
    set(show, 'String', "Show rad");
    mode = 1;
    rad_mode_btn = uicontrol('Style', 'pushbutton', 'String', 'Rad_mode','Position', [20, 360, 100, 20],'Callback',@rad_btn_callback);
    deg_mode_btn = uicontrol('Style', 'pushbutton', 'String', 'Deg_mode','Position', [200, 360, 100, 20],'Callback', @deg_btn_callback);
    
    % sin 输入和输出文本和编辑框
    uicontrol('Style', 'text', 'String', 'sin Input:', 'Position', [20, 300, 150, 20]);
    sin_input_edit = uicontrol('Style', 'edit', 'Position', [180, 300, 100, 20]);
    uicontrol('Style', 'text', 'String', 'sin Output:', 'Position', [300, 300, 100, 20]);
    sin_output_text = uicontrol('Style', 'text', 'String', '', 'Position', [400, 300, 100, 20]);
    % sin 计算按钮和清零按钮
    sin_calculate_btn = uicontrol('Style', 'pushbutton', 'String', 'Calculate', 'Position', [20, 270, 100, 20], 'Callback', @sin_calculate_callback);
    sin_clear_btn = uicontrol('Style', 'pushbutton', 'String', 'Clear', 'Position', [130, 270, 100, 20], 'Callback', @sin_clear_callback);

    % cos 输入和输出文本和编辑框
    uicontrol('Style', 'text', 'String', 'cos Input:', 'Position', [20, 250, 150, 20]);
    cos_input_edit = uicontrol('Style', 'edit', 'Position', [180, 250, 100, 20]);
    uicontrol('Style', 'text', 'String', 'cos Output:', 'Position', [300, 250, 100, 20]);
    cos_output_text = uicontrol('Style', 'text', 'String', '', 'Position', [400, 250, 100, 20]);
    % cos 计算按钮和清零按钮
    cos_calculate_btn = uicontrol('Style', 'pushbutton', 'String', 'Calculate', 'Position', [20, 220, 100, 20], 'Callback', @cos_calculate_callback);
    cos_clear_btn = uicontrol('Style', 'pushbutton', 'String', 'Clear', 'Position', [130, 220, 100, 20], 'Callback', @cos_clear_callback);

    % arcsin 输入和输出文本和编辑框
    uicontrol('Style', 'text', 'String', 'arcsin Input:', 'Position', [20, 200, 150, 20]);
    arcsin_input_edit = uicontrol('Style', 'edit', 'Position', [180, 200, 100, 20]);
    uicontrol('Style', 'text', 'String', 'arcsin Output:', 'Position', [300, 200, 100, 20]);
    arcsin_output_text = uicontrol('Style', 'text', 'String', '', 'Position', [400, 200, 100, 20]);
    % arcsin 计算按钮和清零按钮
    arcsin_calculate_btn = uicontrol('Style', 'pushbutton', 'String', 'Calculate', 'Position', [20, 170, 100, 20], 'Callback', @arcsin_calculate_callback);
    arcsin_clear_btn = uicontrol('Style', 'pushbutton', 'String', 'Clear', 'Position', [130, 170, 100, 20], 'Callback', @arcsin_clear_callback);

    % arctan 输入和输出文本和编辑框
    uicontrol('Style', 'text', 'String', 'arctan Input:', 'Position', [20, 150, 150, 20]);
    arctan_input_edit = uicontrol('Style', 'edit', 'Position', [180, 150, 100, 20]);
    uicontrol('Style', 'text', 'String', 'arctan Output:', 'Position', [300, 150, 100, 20]);
    arctan_output_text = uicontrol('Style', 'text', 'String', '', 'Position', [400, 150, 100, 20]);
    % arctan 计算按钮和清零按钮
    arctan_calculate_btn = uicontrol('Style', 'pushbutton', 'String', 'Calculate', 'Position', [20, 120, 100, 20], 'Callback', @arctan_calculate_callback);
    arctan_clear_btn = uicontrol('Style', 'pushbutton', 'String', 'Clear', 'Position', [130, 120, 100, 20], 'Callback', @arctan_clear_callback);

    % 启用 rad 输出模式
    function rad_btn_callback(~, ~)
        set(show, 'String', "rad mode");
        mode = 1;
    end

    % 启用 deg 输出模式
    function deg_btn_callback(~, ~)
        set(show, 'String', "deg mode");
        mode = 2;
    end
    
    % 计算按钮回调函数
    function sin_calculate_callback(~, ~)
        % 计算 sin
        sin_input = str2double(get(sin_input_edit, 'String'));
        if mode == 1
            obj = py.importlib.import_module('Cal_sin_cos_rad');
            py.importlib.reload(obj);
            result_sin = py.Cal_sin_cos_rad.Calculate_sin(sin_input);
        else
             obj = py.importlib.import_module('Cal_sin_cos_degree');
            py.importlib.reload(obj);
            result_sin = py.Cal_sin_cos_degree.Calculate_sin(sin_input);
        end
        set(sin_output_text, 'String', num2str(result_sin));
    end

    function cos_calculate_callback(~, ~)
        % 计算 cos
        cos_input = str2double(get(cos_input_edit, 'String'));
        if mode == 1
            obj = py.importlib.import_module('Cal_sin_cos_rad');
            py.importlib.reload(obj);
            result_cos = py.Cal_sin_cos_rad.Calculate_cos(cos_input);
        else
            obj = py.importlib.import_module('Cal_sin_cos_degree');
            py.importlib.reload(obj);
            result_cos = py.Cal_sin_cos_degree.Calculate_cos(cos_input);
        end
        set(cos_output_text, 'String', num2str(result_cos));
    end

    function arcsin_calculate_callback(~, ~)
        % 计算 arcsin
        arcsin_input = str2double(get(arcsin_input_edit, 'String'));
        obj = py.importlib.import_module('Arcsin_calc');
        py.importlib.reload(obj);
        result_arcsin = py.Arcsin_calc.Arcsin_calc(arcsin_input);
        if mode == 1
            set(arcsin_output_text, 'String', num2str(cell2mat(result_arcsin(1))));
        else
            set(arcsin_output_text, 'String', num2str(cell2mat(result_arcsin(2))));
        end
    end

    function arctan_calculate_callback(~, ~)
        % 计算 arctan
        arctan_input = str2double(get(arctan_input_edit, 'String'));
        obj = py.importlib.import_module('Calculate_arctan');
        py.importlib.reload(obj);
        result_arctan = py.Calculate_arctan.Calculate_arctan(arctan_input);
        if mode == 1
            set(arctan_output_text, 'String', num2str(cell2mat(result_arctan(1))));
        else
            set(arctan_output_text, 'String', num2str(cell2mat(result_arctan(2))));
        end
    end

    % 清零按钮回调函数
    function sin_clear_callback(~, ~)
        set(sin_input_edit, 'String', '');
        set(sin_output_text,  'String', '');
    end

    function cos_clear_callback(~, ~)
        set(cos_input_edit, 'String', '');
        set(cos_output_text, 'String', '');
    end

    function arcsin_clear_callback(~, ~)
        set(arcsin_input_edit, 'String', '');
        set(arcsin_output_text, 'String', '');
    end

    function arctan_clear_callback(~, ~)
        set(arctan_input_edit, 'String', '');
        set(arctan_output_text, 'String', '');
    end
end