import { Data } from '@/data/Data';
import plotly from 'plotly.js'

export function insertPlot(number: number, data: Data, id?: string, isMobile?: boolean) {
    const plot = JSON.parse(data['plots'][`figure_${number}`]);
    if (isMobile) {
      plot['layout']['showlegend'] = false;
      //plot['layout']['legend'] = { 'orientation': 'h' };
    } else {
      plot['layout']['height'] = 600;
    }
    plot['config'] = {
      responsive: true,
    }
    const idString: string = id === undefined ? `plot${number}` : id;
    plotly.newPlot(idString, plot);
  }