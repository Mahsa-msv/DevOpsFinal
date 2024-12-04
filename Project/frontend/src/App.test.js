import { render, screen } from '@testing-library/react';
import App from './App';

test('renders calculator heading', () => {
  render(<App />);
  const headingElement = screen.getByText(/calculator/i);
  expect(headingElement).toBeInTheDocument();
});
