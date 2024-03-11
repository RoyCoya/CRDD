/* eslint-disable no-undef */

import { render } from '@testing-library/vue'
import HomePage from '@/apps/HomePage/HomePage.vue'

test('it should render the homepage with the correct title', () => {
  const { getByText } = render(HomePage);

  // 断言输出
  getByText('Welcome to My Homepage');
});

test('it should render the homepage with the correct content', () => {
  const { getByText } = render(HomePage);

  // 断言输出
  getByText('This is a simple homepage template created with Vue.js and Vite.');
});

// 可以添加更多的测试用例来测试组件的其他方面
