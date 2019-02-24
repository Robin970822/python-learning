import pandas as pd
import numpy as np


def wyh(filename, regions, names=None):
    data = pd.read_csv(filename, names=names, header=None)
    codes = np.sort(np.unique(data['Code']))
    _data = data.copy()
    _data = _data[~ _data['Importer'].isin(regions)]

    for code in codes:
        total_trade_value = 0
        code_data = data[data['Code'] == code]
        for region in regions:
            region_data = code_data[code_data['Importer'] == region]
            region_trade_value = region_data['TradeValue']
            region_trade_value = region_trade_value[region_trade_value.index[0]] if len(region_trade_value) != 0 else 0
            total_trade_value += region_trade_value
        print code, ': ', total_trade_value
        if total_trade_value != 0:
            _code_data = code_data[code_data['Importer'].isin(regions)].iloc[0].copy()
            _code_data['Importer'] = regions[0]
            _code_data[10] = 'CHN'
            _code_data['TradeValue'] = total_trade_value
            _data = _data.append(_code_data, ignore_index=True)

    _data.to_csv('wyh_out/' + filename, header=True)


if __name__ == '__main__':
    filename = 'Austria_2003_beltroad_4.csv'
    regions = ['China', 'China, Hong Kong SAR', 'China, Macao SAR']
    names = ['Year', '1', '2', '3', '4', '5',
             'Exporter', 'ExporterCode', '8',
             'Importer', 'ImporterCode', 'Code',
             '12', '13', 'TradeValue', '15', '16', '17']
    wyh(filename, regions, names)
