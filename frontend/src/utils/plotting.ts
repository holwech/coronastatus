import { Data } from '@/data/Data';
import plotly from 'plotly.js'

export function insertPlot(figureName: string, data: Data, id: string, isMobile?: boolean) {
    const plot = JSON.parse(data['plots'][figureName]);
    if (isMobile) {
      plot['layout']['showlegend'] = false;
      //plot['layout']['legend'] = { 'orientation': 'h' };
    } else {
      plot['layout']['height'] = 600;
    }
    plot['config'] = {
      responsive: true,
    }
    plotly.newPlot(id, plot);
  }