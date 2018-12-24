import styled from 'styled-components';
import { palette } from 'styled-theme';
import { borderRadius, transition } from '../../settings/style-util';

const ProductComposeBtnWrapper = styled.div`
  width: 100%;
  padding: 0px 30px;
  height: 50px;
  display: flex;
  align-items: center;
  flex-shrink: 0;
  background-color: ${palette('grayscale', 6)};
  border-bottom: 1px solid ${palette('border', 4)};
  
  .isoComposeBtnWrapper {
  }

  button {
    font-size: 14px;
    font-weight: 400;
    color: #ffffff;
    margin: 2px;
    background-color: ${palette('primary', 0)};
    width: 100%;
    height: 30px;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    border: 0;
    outline: 0;
    cursor: pointer;
    ${borderRadius('3px')};
    ${transition()};

    &:hover {
      background-color: ${palette('primary', 1)};
    }
  }
`;

export default ProductComposeBtnWrapper;
